# operationGroup

**Framework**: CloudKit  
**Kind**: property

The operation group to use for the underlying CloudKit operations.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
var operationGroup: CKOperationGroup { get set }
```

#### Discussion

> 💡 **Tip**:  Providing a specific operation group helps you to identify and analyze the telemetry of send operations in CloudKit Console.

The default value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/sendchangesoptions/operationgroup)*