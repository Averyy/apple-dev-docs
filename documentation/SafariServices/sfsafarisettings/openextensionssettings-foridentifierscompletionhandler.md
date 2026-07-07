# openExtensionsSettings(forIdentifiers:completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Presents the extensions pane from Safari Settings.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- visionOS 26.2+

## Declaration

```swift
class func openExtensionsSettings(forIdentifiers extensionIdentifiers: [String]) async throws
```

#### Discussion

The method returns an error unless you call it while your app is in the foreground.

## Parameters

- `extensionIdentifiers`: An array of extension identifiers. If the value is a single identifier, Settings opens to that extension’s detail view. If you specify multiple identifiers, Settings opens to the Safari Extensions pane with the specified extensions selected.
- `completionHandler`: A block the system calls after the operation completes, with an optional error parameter. - **error**: `nil` if Safari Extensions Settings opens successfully; otherwise, an error that indicates the reason for the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafarisettings/openextensionssettings(foridentifiers:completionhandler:))*