# storeIdentifier

**Framework**: SwiftData  
**Kind**: property

The on-disk identifier of the data store this token covers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var storeIdentifier: String { get }
```

#### Discussion

Use with [`configurationName(forStoreIdentifier:)`](modelcontainer/configurationname(forstoreidentifier:).md) to map the identifier back to the [`ModelConfiguration`](modelconfiguration.md) name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historytoken/storeidentifier)*