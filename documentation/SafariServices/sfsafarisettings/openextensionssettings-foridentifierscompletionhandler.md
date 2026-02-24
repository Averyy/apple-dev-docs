# openExtensionsSettings(forIdentifiers:completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Launches Settings to Safari Extensions Settings

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- visionOS 26.2+

## Declaration

```swift
class func openExtensionsSettings(forIdentifiers extensionIdentifiers: [String]) async throws
```

#### Discussion

Call this method when your app is in the foreground, otherwise it returns an error.

Launches Settings to Safari Extensions Settings.

Call this method when your app is in the foreground, otherwise it returns an error.

## Parameters

- `extensionIdentifiers`: An array of extension identifiers. If you specify one identifier, Settings opens to that extension’s detail view. If you specify multiple identifiers, Settings opens to the Safari Extensions pane and highlights those extensions.
- `completionHandler`: The block the system calls after the operation completes, with an optional error parameter if an error occurs. - **error**: An error object indicating the reason for the failure, or `nil` if the system successfully opens to Safari Extensions Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafarisettings/openextensionssettings(foridentifiers:completionhandler:))*