# exposedBindings

**Framework**: Objective-C Runtime  
**Kind**: property

Returns an array containing the bindings exposed by the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
var exposedBindings: [NSBindingName] { get }
```

#### Return Value

An array containing the bindings exposed by the receiver.

#### Discussion

A subclass can override this method to remove bindings that are exposed by a superclass that are not appropriate for the subclass.

## See Also

- [class func exposeBinding(NSBindingName)](nsobject-swift.class/exposebinding(_:).md)
  Exposes the specified `binding`, advertising its availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/exposedbindings)*