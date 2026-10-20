# handleBDXQuery(forNodeID:controller:blockSize:blockIndex:bytesToSkip:completionHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

## Declaration

```swift
optional func handleBDXQuery(forNodeID nodeID: NSNumber, controller: MTRDeviceController, blockSize: NSNumber, blockIndex: NSNumber, bytesToSkip: NSNumber, completionHandler: @escaping @Sendable (Data?, Bool) -> Void)
```

```swift
optional func handleBDXQuery(forNodeID nodeID: NSNumber, controller: MTRDeviceController, blockSize: NSNumber, blockIndex: NSNumber, bytesToSkip: NSNumber) async -> (Data?, Bool)
```

```objc
- (void) handleBDXQueryForNodeID:(NSNumber *) nodeID controller:(MTRDeviceController *) controller blockSize:(NSNumber *) blockSize blockIndex:(NSNumber *) blockIndex bytesToSkip:(NSNumber *) bytesToSkip completionHandler:(void (^)(NSData *data, BOOL isEOF)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrotaproviderdelegate/handlebdxquery(fornodeid:controller:blocksize:blockindex:bytestoskip:completionhandler:))*