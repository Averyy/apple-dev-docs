# attachableValue

**Framework**: Swift Testing  
**Kind**: property

The value of this attachment.

**Availability**:
- Swift 6.2+
- Xcode 17.0+

## Declaration

```swift
var attachableValue: AttachableValue.Wrapped { get }
```

#### Discussion

When the attachable value’s type conforms to [`AttachableWrapper`](attachablewrapper.md), the value of this property equals the wrapper’s underlying attachable value. To access the attachable value as an instance of `T` (where `T` conforms to [`AttachableWrapper`](attachablewrapper.md)), specify the type explicitly:

```swift
let attachableValue = attachment.attachableValue as T
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/attachablevalue-vkrw)*