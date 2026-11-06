# Detecting available Apple Foundation Models

**Framework**: Foundation Models  
**Role**: Article

Discover which Apple Foundation Models your app can use across devices and platforms.

## Overview

Apple Foundation Models (AFM) power Apple Intelligence. You can call AFM models via the Foundation Models framework, and they come built-in to many Apple devices, making AFM a convenient and powerful option for your app. Smaller AFM models run entirely on-device, while the most powerful AFM models run on Private Cloud Compute (PCC). All AFM models are capable of text and image understanding.

| Model | Size | Where it runs | Framework symbol |
| --- | --- | --- | --- |
| AFM Core Advanced | 20 billion parameters, 8K tokens context | on-device | [`SystemLanguageModel`](./systemlanguagemodel.md) |
| AFM Core | 3 billion parameters, 4-8K tokens context | on-device | [`SystemLanguageModel`](./systemlanguagemodel.md) |
| AFM Cloud | 32K tokens context | server | [`PrivateCloudComputeLanguageModel`](./privatecloudcomputelanguagemodel.md) |

To detect which AFM models can run on a person’s device, consider the following:

- **Availability**: Both [`SystemLanguageModel`](./systemlanguagemodel.md) and [`PrivateCloudComputeLanguageModel`](./privatecloudcomputelanguagemodel.md) have availability checks that tell you if the operating system is ready to run the model. For `PrivateCloudComputeLanguageModel`, check additional aspects of availability, including authentication, and the PCC usage quota of the person running your app.
- **Model variant**: [`SystemLanguageModel`](./systemlanguagemodel.md) represents two different AFM on-device variants: AFM Core and AFM Core Advanced. `PrivateCloudComputeLanguageModel` doesn’t have any variants; it only represents AFM Cloud. Use the [`variant`](./systemlanguagemodel/variant-swift.property.md) property at runtime to detect which `SystemLanguageModel` variant is present on a person’s device. Your app won’t be able to pick: each device has a single on-device AFM.

If your app needs to maintain compatibility with older operating system versions, monitor how AFM models change over time:

- **Model version**: Apple occasionally updates AFM on-device models, like AFM Core, as part of a regular operating system update. Like variants, your app won’t be able to pick which model version to use. Check the version present on a person’s device using standard Swift `if #available` checks with the [`variant`](./systemlanguagemodel/variant-swift.property.md) property of [`SystemLanguageModel`](./systemlanguagemodel.md).
- **Context window size**: This number represents how many tokens your app can send a model in a single session. Context window size can vary, even within the same model variant and version. To get the exact number of tokens available, check the [`contextSize`](./systemlanguagemodel/contextsize.md) property of [`SystemLanguageModel`](./systemlanguagemodel.md) and the [`contextSize`](./privatecloudcomputelanguagemodel/contextsize.md) property of [`PrivateCloudComputeLanguageModel`](./privatecloudcomputelanguagemodel.md).

## Create a model instance and check availability

Before running [`SystemLanguageModel`](./systemlanguagemodel.md) or [`PrivateCloudComputeLanguageModel`](./privatecloudcomputelanguagemodel.md), verify that the models can run on the device. For [`SystemLanguageModel`](./systemlanguagemodel.md), start by creating an instance of the default model:

```swift
let model = SystemLanguageModel.default
```

While you can later customize [`SystemLanguageModel`](./systemlanguagemodel.md) to other use cases, such as [`contentTagging`](./systemlanguagemodel/usecase/contenttagging.md), those aren’t available unless the default [`general`](./systemlanguagemodel/usecase/general.md) use case is available, so check `.default` first.

Creating an instance of [`PrivateCloudComputeLanguageModel`](./privatecloudcomputelanguagemodel.md) starts an authentication and readiness check with the operating system and the server. Authentication fails (and logs a warning) if your app doesn’t have the [`com.apple.developer.private-cloud-compute`](../BundleResources/entitlements/com.apple.developer.private-cloud-compute.md) entitlement. For the best performance, create a single `PrivateCloudComputeLanguageModel` instance and share it across your app so you only call these checks once:

```swift
// Logs a warning if the entitlement is missing.
let pccModel = PrivateCloudComputeLanguageModel()
```

Next, check for availability. The [`SystemLanguageModel`](./systemlanguagemodel.md) and [`PrivateCloudComputeLanguageModel`](./privatecloudcomputelanguagemodel.md) classes each provide two properties for availability, following the same shape. Use `.isAvailable` for a quick Boolean check:

```swift
let model = SystemLanguageModel.default
if model.isAvailable {
    // The model is ready to use.
}
```

Or, use `.availability` to discover why the model is unavailable. Each model has its own `.unavailable` cases designed to give you the information you need to communicate with the person running your app. For example, [`SystemLanguageModel`](./systemlanguagemodel.md) has these cases:

```swift
let logger = Logger(subsystem: "com.example.MyApp", category: "ModelAvailability")

switch model.availability {
case .available:
    logger.info("The model is available and ready to use.")
case .unavailable(.deviceNotEligible):
    logger.info("The model isn't downloaded and cannot run on this device.")
case .unavailable(.appleIntelligenceNotEnabled):
    logger.info("Apple Intelligence isn't enabled on the device.")
case .unavailable(.modelNotReady):
    logger.info("The model isn't ready due to download or system reasons.")
@unknown default:
    logger.info("The model is unavailable for a reason added after you wrote this code.")
}
```

Meanwhile, [`PrivateCloudComputeLanguageModel`](./privatecloudcomputelanguagemodel.md) has these cases:

```swift
switch pccModel.availability {
case .available:
    logger.info("The PCC model is available and ready to use.")
case .unavailable(.deviceNotEligible):
    logger.info("The device doesn't support Apple Intelligence.")
case .unavailable(.systemNotReady):
    logger.info("The system isn't yet ready to serve PCC requests.")
@unknown default:
    logger.info("The PCC model is unavailable for a reason added after you wrote this code.")
}
```

An easy mistake to make is that [`PrivateCloudComputeLanguageModel`](./privatecloudcomputelanguagemodel.md) returns `.available` even if your app isn’t permitted to run the model. This is because availability checks whether `PrivateCloudComputeLanguageModel` is ready to run at the operating system level, but it assumes you’re already authenticated because creating a `PrivateCloudComputeLanguageModel` instance would’ve automatically performed an authentication check. For the system to authenticate your app with PCC, your app must have the [`com.apple.developer.private-cloud-compute`](../BundleResources/entitlements/com.apple.developer.private-cloud-compute.md) entitlement. Without the PCC entitlement, your app crashes with a fatal error when you send the model a prompt for the first time.

For [`PrivateCloudComputeLanguageModel`](./privatecloudcomputelanguagemodel.md), check whether the person using your app has enough of their daily quota left to access PCC, use [`quotaUsage`](./privatecloudcomputelanguagemodel/quotausage-swift.property.md). After you’ve checked model availability, treat the quota as a final extra availability check:

```swift
if pccModel.quotaUsage.isLimitReached {
    // The PCC model is unavailable for the rest of the day.
} else {
    // The PCC model is ready to use.
}
```

For more on how the quota works, when it resets, and what your app can do, see [Adding server-side intelligence with Private Cloud Compute](./adding-server-side-intelligence-with-private-cloud-compute.md).

## Handle different unavailable reasons

When your availability check returns `.unavailable`, the model won’t run. The steps you take to solve the problem depend on the unavailability reason that the `.available` property provides:

- **`.appleIntelligenceNotEnabled`**: This unavailable reason occurs in iOS 26, iPadOS 26, macOS 26, and visionOS 26 or later. To fix, ask the person using your app to go to the Settings app and turn on Apple Intelligence.

> **Note**: In iOS 27, iPadOS 27, macOS 27, and visionOS 27 or later, Apple Intelligence is on by default and can no longer be turned off.

- **`.modelNotReady` or `.systemNotReady`**: These unavailable reasons resolve on their own after the OS finishes some necessary work. Most commonly you encounter `.modelNotReady` from [`SystemLanguageModel`](./systemlanguagemodel.md) while the model is downloading. When a person updates their device, the operating system sometimes updates the model assets, which can take a while to download and prepare. You may also see `.systemNotReady` from [`PrivateCloudComputeLanguageModel`](./privatecloudcomputelanguagemodel.md) briefly after an update. For either case, present an alert that says the feature is temporarily unavailable, and ask the person to try again later.
- **`.deviceNotEligible`**: This is the most challenging unavailability case for your app, because it means the person’s device doesn’t support Apple Intelligence and can’t use AFM. The person can fix certain eligibility issues quickly by changing their device’s settings or freeing up storage space. It’s best to let a person figure out if any of those scenarios apply to them.

  If a person successfully turns on Apple Intelligence for their device, your app may get the `.modelNotReady` or `.systemNotReady` cases for a while afterwards while the operating system loads Apple Intelligence onto the device.

Ultimately, your app may run on devices that aren’t compatible with any version of AFM. But that doesn’t mean you need to turn off your feature entirely. For these situations, consider whether your app can use a different model as backup, such as another server-based large language model. Alternatively, consider a custom on-device model, as described in [Running a Core AI model in a Foundation Models session](./running-a-core-ai-model-in-a-foundation-models-session.md).

## Detect the exact model variant and version

After confirming model availability, your app can start calling the model. For [`PrivateCloudComputeLanguageModel`](./privatecloudcomputelanguagemodel.md), the AFM Cloud model is the same no matter which device or OS version you call it from, allowing you to use the same prompt across everywhere your app ships.

AFM Cloud occasionally updates to improve quality and performance, and these updates can occur at any time. You may need to occasionally update your prompt to maintain the best quality, but you won’t need to maintain older prompt versions: after AFM Cloud updates, it’s updated for everyone.

Treat [`SystemLanguageModel`](./systemlanguagemodel.md) as a single model, but you’ll often get the highest quality if you customize your app’s feature to the specific model present. There are currently two `SystemLanguageModel` variants: AFM Core Advanced and AFM Core, as noted in the table earlier.

The [`SystemLanguageModel`](./systemlanguagemodel.md) defines “the system’s language model.” Every device has just one `SystemLanguageModel`, so your app can’t choose which variant or version to use. That’s because even a small foundation model is a large asset in storage and memory. To protect a device’s performance, the operating system ensures a single on-device AFM is present. People may have AFM Core or AFM Core Advanced on their device, but not both. Similarly, each device has a single version of the model downloaded, so your app runs with whichever model is present.

This table shows the versions of [`SystemLanguageModel`](./systemlanguagemodel.md) your app may encounter:

| OS version | Models | Read about this update |
| --- | --- | --- |
| iOS 27.0, iPadOS 27.0, macOS 27.0, and visionOS 27.0 or later | AFM 3 Core, AFM 3 Core Advanced | [Introducing the Third Generation of Apple’s Foundation Models](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) |
| iOS 26.4, iPadOS 26.4, macOS 26.4, and visionOS 26.4 or later | AFM 2.1 Core | [Foundation Models updates](../Updates/foundationmodels.md) |
| iOS 26.0, iPadOS 26.0, macOS 26.0, and visionOS 26.0 or later | AFM 2 Core | [Updates to Apple’s On-Device and Server Foundation Language Models](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) |

To determine the exact model present, use a runtime check. In iOS 27, iPadOS 27, macOS 27, and visionOS 27 or later, read the [`variant`](./systemlanguagemodel/variant-swift.property.md) property, which returns a [`SystemLanguageModel.Variant`](./systemlanguagemodel/variant-swift.struct.md). For earlier releases, use a standard Swift `if #available` check, starting from the newest release and ending with the oldest:

```swift
let logger = Logger(subsystem: "com.example.MyApp", category: "ModelVariant")

// In iOS 27, iPadOS 27, macOS 27, and visionOS 27 or later, use the `variant` property.
if #available(iOS 27.0, iPadOS 27.0, macOS 27.0, visionOS 27.0, *) {
    let variant = SystemLanguageModel.default.variant
    switch variant {
    case .core3:
        // This logs AFM 3 Core.
        logger.info("Model detected: \(variant.displayName)")
    case .coreAdvanced3:
        // This logs AFM 3 Core Advanced.
        logger.info("Model detected: \(variant.displayName)")
    default:
        logger.warning("Detected an unrecognized model variant: \(variant.displayName)")
    }
} else if #available(iOS 26.4, iPadOS 26.4, macOS 26.4, visionOS 26.4, *) {
    // iOS 26.4, iPadOS 26.4, macOS 26.4, and visionOS 26.4 or later have AFM 2.1 Core.
    logger.info("Model detected: AFM 2.1 Core")
} else {
    // iPadOS 26.0 to 26.3, macOS 26.0 to 26.3, and visionOS 26.0 to 26.3 have AFM 2 Core.
    logger.info("Model detected: AFM 2 Core")
}
```

For more information about adapting your app for different model variants and versions, see [Updating prompts for new model versions](./updating-prompts-for-new-model-versions.md).

## Check model-device compatibility

Use the following table as a quick reference to the devices that can run Apple Foundation Models, but remember that language, region, and device storage space requirements also affect availability. For the most up-to-date information, including the latest list of supported languages, see [How to get the next generation of Apple Intelligence](https://support.apple.com/en-us/121115).

| Platform | Devices | AFM Core | AFM Core Advanced | AFM Cloud |
| --- | --- | --- | --- | --- |
| iPhone | iPhone 15 Pro models, all iPhone 16 models, iPhone 17 | ✅ | ❌ | ✅ |
| iPhone | iPhone Air, iPhone 17 Pro models | iOS 26 | iOS 27 | ✅ |
| iPhone | iPhone 18 Pro models, iPhone Duo | ❌ | ✅ | ✅ |
| iPad | iPad mini (A17 Pro), iPad models with M1 or later | ✅ | ❌ | ✅ |
| iPad | iPad models with M4 or later | iPadOS 26 | iPadOS 27 | ✅ |
| Mac | Mac models with M1 or later, MacBook Neo (A18 Pro) | ✅ | ❌ | ✅ |
| Mac | Mac models with M3 or later | macOS 26 | macOS 27 | ✅ |
| Apple Vision Pro | Apple Vision Pro (M2 or later) | ✅ | ❌ | ✅ |
| Apple Vision Pro | Apple Vision Pro (M5) | visionOS 26 | visionOS 27 | ✅ |
| Apple Watch | SE 3, Series 9 or later, Ultra 2 or later | ❌ | ❌ | ✅ |

> **Note**: A compatible Apple Watch must be paired with an Apple Intelligence-enabled iPhone to run AFM Cloud.

Devices compatible with both AFM Core and AFM Core Advanced run AFM Core on iOS 26.0 to 26.3, iPadOS 26.0 to 26.3, macOS 26.0 to 26.3, and visionOS 26.0 to 26.3, and AFM Core Advanced on iOS 27.0, iPadOS 27.0, macOS 27.0, and visionOS 27.0 or later. The system downloads the best available model, so it downloads AFM Core Advanced when possible, because it’s the more powerful model.

## See Also

### Apple Foundation Models
- [class SystemLanguageModel](./systemlanguagemodel.md)
  An on-device Apple Foundation Model capable of text generation tasks.
- [class PrivateCloudComputeLanguageModel](./privatecloudcomputelanguagemodel.md)
  A variant of Apple Foundation Models that runs on Private Cloud Compute to provide enhanced capabilities while maintaining privacy guarantees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/detecting-available-apple-foundation-models)*