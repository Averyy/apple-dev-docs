# handleBDXTransferSessionBegin(forNodeID:controller:fileDesignator:offset:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
optional func handleBDXTransferSessionBegin(forNodeID nodeID: NSNumber, controller: MTRDeviceController, fileDesignator: String, offset: NSNumber, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
optional func handleBDXTransferSessionBegin(forNodeID nodeID: NSNumber, controller: MTRDeviceController, fileDesignator: String, offset: NSNumber) async throws
```

```objc
- (void) handleBDXTransferSessionBeginForNodeID:(NSNumber *) nodeID controller:(MTRDeviceController *) controller fileDesignator:(NSString *) fileDesignator offset:(NSNumber *) offset completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrotaproviderdelegate/handlebdxtransfersessionbegin(fornodeid:controller:filedesignator:offset:completion:))*