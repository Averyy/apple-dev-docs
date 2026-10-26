---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/init(_:)"
framework: "swift-log/Logging"
---

# init(_:)

**Framework**: swift-log/Logging  
**Kind**: init  
**Role**: Initializer

Create a multiplex log handler.

## Declaration

```swift
init(_ handlers: [any LogHandler])
```

## Parameters

- `handlers`: An array of `LogHandler`s, each of which will receive the log messages sent to this `Logger`. The array must not be empty.

## See Also

### Creating a multiplex log handler
- [init([any LogHandler], metadataProvider: Logger.MetadataProvider?)](./init%28_,metadataprovider%29.md)
  Create a multiplex log handler with the metadata provider you provide.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/init(_:))*