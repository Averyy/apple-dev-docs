# Creating an audio unit extension

**Framework**: AVFAudio

Build an extension by using an Xcode template.

#### Overview

An audio unit extension provides a way to create or modify audio and MIDI data in a multiplatform app that uses sound — including music production apps. It contains the audio unit and, optionally, a user interface to control the audio unit. The audio unit is a custom plug-in where you generate audio or implement an audio-processing algorithm.

To create an audio unit extension, you create an Xcode project using the Audio Unit Extension App template.

##### Create a New Audio Unit Extension Project

To create a new project in Xcode, choose File > New > Project. In the template chooser, select multiplatform. Scroll to the end of the template chooser and select the Audio Unit Extension App template under the Application section.

![A screenshot of the Choose a template for your new project dialog in Xcode. It shows a section with the name Other, with the Audio Unit Extension App template selected.](https://docs-assets.developer.apple.com/published/6132dee6798f52f5961f880013b9a053/updated-media-4093016%402x.png)

After clicking Next, configure the options for the project — including choosing what kind of audio unit to generate.

##### Configure the Project Options

Configure the options for your new audio unit extension application. The template creates an extension and a host application for your audio unit.

![A screenshot of the Choose options for your new project dialog in Xcode. The fields for Product Name, Team, Organization Name, Subtype Code, Manufacturer Code, Testing System, and Storage are empty. The Organization Identifier field contains com.examples. It shows a menu to select the Audio Unit Type, with Effect selected by default. It shows a User Interface menu, with Presents User Interface selected by default. Below the User Interface option, a checkbox for host in CloudKit is unchecked. At the bottom of the dialog, there are three buttons: Cancel, Previous, and Next. The Next button is grayed out. ](https://docs-assets.developer.apple.com/published/007da1182f1ed60fc7d9da1e694d485d/updated-media-4093019%402x.png)

For an Audio Unit Extension App template, Xcode provides a starting point for the type of audio unit you’re creating.

Choose a subtype code that reflects the type of extension, and a manufacturer code that’s unique to your company.

If your extension doesn’t need a user interface, choose No User Interface; otherwise, Xcode creates a view for you to customize.

##### Explore the Generated Extension Project

Xcode generates two targets for you — the host app and the extension. The template uses Swift and SwiftUI for the business logic and user interface, C++ for real-time processing, and Objective-C for interacting between Swift and C++.

![A screenshot of the Xcode Project navigator showing a project with the name NewAU. The project is expanded and shows a host app group and NewAU Extension group, with the extension group expanded. The extension group contains expanded groups with the names Common, Parameters, DSP, and UI. The Common group shows an expanded Audio Unit group with a file named NewAUExtensionAudioUnit. The expanded Parameters group shows the files NewAUExtensionParameterAddresses and Parameters. The expanded DSP group shows the file NewAUExtensionDSPKernel. The expanded UI group shows the files NewAUExtensionMainView and ParameterSlider.](https://docs-assets.developer.apple.com/published/34e04dd1bbac682579564c42b2f21b13/updated-media-4093014%402x.png)

The Common group contains code — organized by functionality — that you rarely need to change. In the above image, the project name `NewAU` is prefixed to many files.

In most cases, you only need to edit the extension files within the top-level groups Parameters, DSP, and UI.

##### Add a New Parameter Address

The template project contains a parameter that allows you to adjust the audio gain. To add a signal parameter to the template project, navigate to `NewAUExtensionParameterAddress.h` and add it to the enumeration.

```c
typedef NS_ENUM(AUParameterAddress, NewAUExtensionParameterAddress) {
    gain = 0,
    attack
}
```

To allow your host app to interact with the parameter, describe its default value, value range, name, and identifier in `Parameters.swift`. The identifier value you specify is what you use to reference the parameter from your host app.

```swift
ParameterSpec(address: .attack,
              identifier: "attack",
              name: "Attack",
              units: .milliseconds,
              valueRange: 0.0…1000.0,
              defaultValue: 100.0)
```

Navigate to `NewAUExtensionDSPKernel.hpp` to expose the parameter for digital signal processing. Add the custom member variable at the end of the source file, and use the `setParameter` and `getParameter` functions to access it.

```c++
void setParameter(AUParameterAddress address, AUValue value) {
    switch (address) {
        case NewAUExtensionParameterAddress::attack:
            mAttack = value;
    }
}

AUValue getParameter(AUParameterAddress address) {
    switch (address) {
        case NewAUExtensionParameterAddress::attack:
            return (AUValue)mAttack;
        default:
            return 0.f;
    }
}
```

Use the `process` function to implement your custom signal-processing algorithm. For audio units that present a user interface, you access the parameter by using the `parameterTree` value in the main view.

```swift
// Get the attack parameter value.
value.let attack = parameterTree.global.attack.value

// Set the attack parameter value.
value.parameterTree.global.attack.value = 0.5

// Bind the parameter to a slider.
var body: some Value {
    ParameterSlider(param: parameterTree.global.attack)
}
```

## See Also

- [Using voice processing](using-voice-processing.md)
  Add voice-processing capabilities to your app by using audio engine.
- [class AVAudioUnit](avaudiounit.md)
  A subclass of the audio node class that, processes audio either in real time or nonreal time, depending on the type of the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/creating-an-audio-unit-extension)*