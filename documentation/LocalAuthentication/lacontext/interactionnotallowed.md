# interactionNotAllowed

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether authentication can be interactive.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var interactionNotAllowed: Bool { get set }
```

```objc
@property (nonatomic) BOOL interactionNotAllowed;
```

## See Also

### Evaluating access controls
- [func evaluateAccessControl(SecAccessControl, operation: LAAccessControlOperation, localizedReason: String, reply: (Bool, (any Error)?) -> Void)](./evaluateaccesscontrol%28_,operation,localizedreason,reply%29.md)
  Evaluates an access control for a given operation.
- [enum LAAccessControlOperation](../laaccesscontroloperation.md)
  Operations to be evaluated for access control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/interactionnotallowed)*