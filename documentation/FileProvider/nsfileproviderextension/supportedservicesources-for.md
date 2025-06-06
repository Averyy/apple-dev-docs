# supportedServiceSources(for:)

**Framework**: File Provider  
**Kind**: method

Return an array of service sources that let the host app perform actions associated with the specified item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func supportedServiceSources(for itemIdentifier: NSFileProviderItemIdentifier) throws -> [any NSFileProviderServiceSource]
```

## See Also

- [protocol NSFileProviderServiceSource](nsfileproviderservicesource.md)
  A service that provides a custom communication channel between the host app and the File Provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/supportedservicesources(for:))*