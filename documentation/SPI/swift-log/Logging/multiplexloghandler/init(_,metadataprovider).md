---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/init(_:metadataprovider:)"
framework: "swift-log/Logging"
---

# init(_:metadataProvider:)

**Framework**: swift-log/Logging  
**Kind**: init  
**Role**: Initializer

Create a multiplex log handler with the metadata provider you provide.

## Declaration

```swift
init(_ handlers: [any LogHandler], metadataProvider: Logger.MetadataProvider?)
```

## Parameters

- `handlers`: An array of `LogHandler`s, each of which will receive every log message sent to this `Logger`. The array must not be empty.
- `metadataProvider`: The metadata provider that adds metadata to log messages for this handler.

## See Also

### Creating a multiplex log handler
- [init([any LogHandler])](./init%28_%29.md)
  Create a multiplex log handler.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/init(_:metadataprovider:))*