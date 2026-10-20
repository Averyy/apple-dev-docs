# valueClassForBinding(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns the class of the value that will be returned for the specified binding.

**Availability**:
- macOS

## Declaration

```swift
func valueClassForBinding(_ binding: NSBindingName) -> AnyClass?
```

```objc
- (Class) valueClassForBinding:(NSBindingName) binding;
```

#### Return Value

The class of the value that will be returned for `binding`.

#### Discussion

This method is used by Interface Builder to determine the appropriate transformers for a binding.

Implementation of this method is optional.

## Parameters

- `binding`: The name of a binding.

## See Also

### Managing bindings
- [func bind(NSBindingName, to: Any, withKeyPath: String, options: [NSBindingOption : Any]?)](./bind%28_,to,withkeypath,options%29.md)
  Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.
- [func optionDescriptionsForBinding(NSBindingName) -> [NSAttributeDescription]](./optiondescriptionsforbinding%28_%29.md)
  Returns an array describing the options for the specified binding.
- [func infoForBinding(NSBindingName) -> [NSBindingInfoKey : Any]?](./infoforbinding%28_%29.md)
  Returns a dictionary describing the receiver’s `binding`.
- [struct NSBindingInfoKey](../../AppKit/nsbindinginfokey.md)
- [func unbind(NSBindingName)](./unbind%28_%29.md)
  Removes a given binding between the receiver and a controller.
- [func NSIsControllerMarker(Any?) -> Bool](../../AppKit/nsiscontrollermarker%28_%29.md)
  Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/valueclassforbinding(_:))*