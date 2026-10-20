# exposeBinding(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Exposes the specified `binding`, advertising its availability.

**Availability**:
- macOS

## Declaration

```swift
class func exposeBinding(_ binding: NSBindingName)
```

```objc
+ (void) exposeBinding:(NSBindingName) binding;
```

#### Discussion

The bound property will be accessed using key-value-coding compliant methods. This method is typically invoked in the class’s `initialize` implementation.

Bindings exposed using `exposeBinding` will be exposed automatically in [`exposedBindings`](./exposedbindings.md) unless that method explicitly filters them out, for example in subclasses.

## Parameters

- `binding`: The key path for the property to be exposed.

## See Also

### Exposing bindings
- [var exposedBindings: [NSBindingName]](./exposedbindings.md)
  Returns an array containing the bindings exposed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/exposebinding(_:))*