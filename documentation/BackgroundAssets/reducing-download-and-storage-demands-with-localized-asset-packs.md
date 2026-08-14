# Reducing download and storage demands with localized asset packs

**Framework**: Background Assets

Improve peoples’ experience of your app by downloading only immediately needed language assets.

#### Overview

In macOS 27, iOS 27, tvOS 27, and visionOS 27, asset packs support a `language` designation. Compared to asset packs that support many languages, localized asset packs download faster, and take up less storage on the device. Use language-specific asset packs to deliver a better experience in your app.

##### Create Localized Asset Packs

As described in [`Creating managed asset packs`](creating-managed-asset-packs.md), use the Terminal command `xcrun ba-package template` to create an asset pack template as a JSON file. Beginning in Xcode 27, the JSON entries in the generated file contains a key named `language`.

For the `language` key’s value, provide a language identifier string as an ISO-639 language code. You can include additional tags from the BCP-47 specification, such as region or script. The following table shows some example values for the `language` key:

| BCP-47 identifier | Meaning |
| --- | --- |
| `ja` | Japanese, for any region. |
| `es-US` | Spanish, for the `US` region. |
| `zh-Hant` | Chinese, using Traditional script. |
| `zh-Hans-VN` | Chinese, using Simplified script, as used in Vietnam. |

Don’t use variant subtags or any extensions to the BCP-47 standard; Background Assets only supports language, region, and script.

##### Download Localized Asset Packs

Host your localized asset packs on App Store Connect to make them available to your app. You can inspect available localized asset packs in Swift by acessing the [`manifest`](assetpackmanager/manifest.md) property of [`AssetPackManager`](assetpackmanager.md). The [`AssetPackManifest`](assetpackmanifest.md) property [`localizedAssetPacks`](assetpackmanifest/localizedassetpacks.md) provides a set of asset packs that best matches the language preferences in Settings or System Settings. In Objective-C, use the [`BAAssetPackManager`](baassetpackmanager.md) method [`getManifestWithCompletionHandler:`](baassetpackmanager/getmanifestwithcompletionhandler:.md) and the [`BAAssetPackManifest`](baassetpackmanifest.md) property [`localizedAssetPacks`](baassetpackmanifest/localizedassetpacks.md) to get the set of localized asset packs.

If your app doesn’t provide its own language-selection interface, you can use the [`AssetPackManager`](assetpackmanager.md) property [`resolvedLanguage`](assetpackmanager/resolvedlanguage.md) to determine the needed language. By default, this property represents the best match between the languages available in the app’s localized asset packs and the language currently selected in the Settings or System Settings app. The manifest also provides a [`resolvedLanguage`](assetpackmanifest/resolvedlanguage.md) read-only property with similar semantics.

When you know the language for which you want to download an asset pack, get the localized asset pack instance from the manifest, and call the manager’s [`ensureLocalAvailability(of:requireLatestVersion:)`](assetpackmanager/ensurelocalavailability(of:requirelatestversion:).md) method with the asset pack. As described in [`Downloading Apple-hosted asset packs`](downloading-apple-hosted-asset-packs.md), this method downloads the specified asset pack, or returns quickly if the asset pack is already downloaded.

The API is similar in Objective-C: you can get the [`resolvedLanguage`](baassetpackmanager/resolvedlanguage.md) from the [`BAAssetPackManager`](baassetpackmanager.md), then call [`ensureLocalAvailabilityOfAssetPack:completionHandler:`](baassetpackmanager/ensurelocalavailabilityofassetpack:completionhandler:.md).

##### Specify One or More Languages

If your app provides its own language-selection interface, you can override the default behavior and fetch assets for languages that don’t necessarily match the current system selection. The [`resolvedLanguage`](assetpackmanager/resolvedlanguage.md) property of [`AssetPackManager`](assetpackmanager.md) is read/write: you can set the value to indicate you want to use a different language. If you want to revert to system defaults later, set this property to `nil`.

Setting the property doesn’t download or remove asset packs. Call [`reconcilePreferredLanguages()`](assetpackmanager/reconcilepreferredlanguages().md) to download any needed asset packs and remove the ones that aren’t.

In Objective-C, the [`BAAssetPackManager`](baassetpackmanager.md) provides an equivalent [`resolvedLanguage`](baassetpackmanager/resolvedlanguage.md) property and a [`reconcilePreferredLanguagesWithCompletionHandler:`](baassetpackmanager/reconcilepreferredlanguageswithcompletionhandler:.md) method.

Some apps need to support multiple languages at the same time. For example, a game might show cutscene videos with audio tracks in a small number of languages, but offer subtitles and menu text in many more languages. In this case, you’d look up the asset packs for each needed language, and then call the manager’s [`ensureLocalAvailability(of:requireLatestVersions:)`](assetpackmanager/ensurelocalavailability(of:requirelatestversions:).md) method, passing in a [`Set`](https://developer.apple.com/documentation/swift/set) of language-specific asset packs. Calling this method allows Background Assets to download any missing asset packs as a batch, which performs better than making separate calls to [`ensureLocalAvailability(of:requireLatestVersion:)`](assetpackmanager/ensurelocalavailability(of:requirelatestversion:).md) for each asset pack.

If any of the downloads fail, this method throws [`AssetPackManager.LocalAvailabilityError`](assetpackmanager/localavailabilityerror.md), which contains a set of [`successes`](assetpackmanager/localavailabilityerror/successes.md), as well as a [`failures`](assetpackmanager/localavailabilityerror/failures.md) dictionary that maps asset packs to error instances that describe the reason for the failure.

In Objective-C, the equivalent method is [`ensureLocalAvailabilityOfAssetPacks:requireLatestVersions:completionHandler:`](baassetpackmanager/ensurelocalavailabilityofassetpacks:requirelatestversions:completionhandler:.md), which provides an [`NSError`](https://developer.apple.com/documentation/foundation/nserror) to the completion handler if downloading fails.

##### Retrieve Content From Localized Asset Packs

[`AssetPackManager`](assetpackmanager.md) provides methods to fetch the contents of an asset by passing in a [`FilePath`](https://developer.apple.com/documentation/system/filepath)  within the asset pack, returning either [`Data`](https://developer.apple.com/documentation/foundation/data), a [`FileDescriptor`](https://developer.apple.com/documentation/system/filedescriptor), or a [`URL`](https://developer.apple.com/documentation/foundation/url). When supporting multiple languages with multiple localized asset packs, you may need to specify the language. For example, in the game scenario described above, several asset packs might have an entry at `videos/openingmovie.m4v`, and searching by just the file path is ambiguous. To handle the ambiguity, call the variants of the content-access methods that contain an “as localized for” parameter, as summarized in the following table:

| [`AssetPackManager`](assetpackmanager.md) (Swift) | [`BAAssetPackManager`](baassetpackmanager.md) (Objective-C) |
| --- | --- |
| [`contents(at:asLocalizedFor:options:)`](assetpackmanager/contents(at:aslocalizedfor:options:).md) | [`contentsAtPath:asLocalizedForLanguage:options:error:`](baassetpackmanager/contentsatpath:aslocalizedforlanguage:options:error:.md) |
| [`descriptor(for:asLocalizedFor:)`](assetpackmanager/descriptor(for:aslocalizedfor:).md) | [`fileDescriptorForPath:asLocalizedForLanguage:error:`](baassetpackmanager/filedescriptorforpath:aslocalizedforlanguage:error:.md) |
| [`url(for:asLocalizedFor:)`](assetpackmanager/url(for:aslocalizedfor:).md) | [`URLForPath:asLocalizedForLanguage:error:`](baassetpackmanager/urlforpath:aslocalizedforlanguage:error:.md) |

The following example demonstrates a helper method from an app that shows an introduction movie, potentially with subtitles in a different language than the audio track contained in the movie file. The method takes the two languages and tries to find their localized asset packs with [`localizedAssetPacks(for:)`](assetpackmanifest/localizedassetpacks(for:).md). Since asset packs require unique identifiers, this example assumes the packs use IDs of the form `intro-movie-en`, `intro-movie-fr`, and so on, and just matches the `intro-movie` substring. If the calls to [`localizedAssetPacks(for:)`](assetpackmanifest/localizedassetpacks(for:).md) find the asset packs, the code creates a set of the asset packs and calls [`ensureLocalAvailability(of:requireLatestVersions:)`](assetpackmanager/ensurelocalavailability(of:requirelatestversions:).md) to check if the assets packs are already on device, and download them if not. Finally, it calls [`url(for:asLocalizedFor:)`](assetpackmanager/url(for:aslocalizedfor:).md) to search the asset packs for a combination of the known file path and the appropriate language, returning a tuple of [`URL`](https://developer.apple.com/documentation/foundation/url)s.

```swift
private func loadIntroMovie(movieLanguage: Locale.Language,
                            subtitleLanguage: Locale.Language) async throws -> (URL, URL) {
    // Ensure availability of movie and subtitle asset packs in their
    // respective languages, downloading if necessary.
    guard let movieAssetPack = try await AssetPackManager.shared.manifest
        .localizedAssetPacks(for: movieLanguage)
        .first(where: {$0.id.starts(with: "intro-movie")})
    else {
        throw MyMissingAssetPackError(id: "intro-movie", language: movieLanguage)
    }
    guard let subtitleAssetPack = try await AssetPackManager.shared.manifest
        .localizedAssetPacks(for: subtitleLanguage)
        .first(where: {$0.id.starts(with: "intro-subtitles")})
    else {
        throw MyMissingAssetPackError(id: "intro-subtitles", language: subtitleLanguage)
        }
    try await AssetPackManager.shared
        .ensureLocalAvailability(of: [movieAssetPack, subtitleAssetPack])

    // Load contents by fetching URLs for the intro movie and its subtitles,
    // screening by language under the assumption that each localized asset
    // pack has equivalent contents, so a given file path may be ambiguous.
    let movieURL = try AssetPackManager.shared
        .url(for: "videos/intro-movie.m4v",
             asLocalizedFor: movieLanguage)
    let subtitleURL = try AssetPackManager.shared
        .url(for: "videos/intro-subtitles.vtt",
             asLocalizedFor: subtitleLanguage)
    return(movieURL, subtitleURL)
}
```

For simplicity, this example doesn’t include a user interface. In a real-world app, it’s important to update the UI with the progress of the download. You might add that functionality by iterating over the asset pack manager’s asynchronous sequence [`statusUpdates(forAssetPackWithID:)`](assetpackmanager/statusupdates(forassetpackwithid:).md) and using the received statuses to update the app’s interface with current progress values.

## See Also

- [Creating managed asset packs](creating-managed-asset-packs.md)
  Create managed asset packs, choose download options, and upload Apple-hosted asset packs  to App Store Connect.
- [Downloading Apple-hosted asset packs](downloading-apple-hosted-asset-packs.md)
  Configure your project and write the code to download asset packs hosted by Apple.
- [Testing asset packs locally](testing-asset-packs-locally.md)
  Test your system-managed asset packs using a mock server on your Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/reducing-download-and-storage-demands-with-localized-asset-packs)*