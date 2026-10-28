---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct/accesskind-swift.enum/watch"
framework: "swift-configuration/Configuration"
---

# AccessEvent.Metadata.AccessKind.watch

**Framework**: swift-configuration/Configuration  
**Kind**: case  
**Role**: Case

An asynchronous watch operation that monitors value changes.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
case watch
```

## Discussion

The async sequence generates a separate event for each value update.

## See Also

### Kinds of configuration access
- [AccessEvent.Metadata.AccessKind.get](./get.md)
  A synchronous get operation that returns the current value.
- [AccessEvent.Metadata.AccessKind.fetch](./fetch.md)
  An asynchronous fetch operation that retrieves the latest value.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct/accesskind-swift.enum/watch)*