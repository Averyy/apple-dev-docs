# exposedBindings

**Framework**: Objective-C Runtime  
**Kind**: property  
**Role**: Instance Property

Returns an array containing the bindings exposed by the receiver.

**Availability**:
- macOS

## Declaration

```swift
var exposedBindings: [NSBindingName] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * exposedBindings;
```

## Return Value

An array containing the bindings exposed by the receiver.

## Discussion

A subclass can override this method to remove bindings that are exposed by a superclass that are not appropriate for the subclass.

## See Also

### Exposing bindings
- [class func exposeBinding(NSBindingName)](./exposebinding%28_%29.md)
  Exposes the specified `binding`, advertising its availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/exposedbindings)*