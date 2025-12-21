# systemExtensions(forApplicationWithBundleID:)

**Framework**: System Extensions  
**Kind**: method

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
func systemExtensions(forApplicationWithBundleID bundleID: String) throws -> Set<OSSystemExtensionProperties>
```

#### Return Value

A set of system extension property objects on success, nil otherwise.

#### Discussion

Get information about system extension(s) in an app with a bundle identifier

## Parameters

- `bundleID`: BundleIdentifier of the application containing the system extension(s)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionsworkspace/systemextensions(forapplicationwithbundleid:))*