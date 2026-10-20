# infoForBinding(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary describing the receiver’s `binding`.

**Availability**:
- macOS

## Declaration

```swift
func infoForBinding(_ binding: NSBindingName) -> [NSBindingInfoKey : Any]?
```

```objc
- (NSDictionary<NSString *,id> *) infoForBinding:(NSBindingName) binding;
```

#### Return Value

A dictionary with information about `binding`, or `nil` if the binding is not bound. The dictionary contains three key/value pairs: `NSObservedObjectKey`: object bound, `NSObservedKeyPathKey`: key path bound, `NSOptionsKey`: dictionary with the options and their values for the bindings.

#### Discussion

This method is mostly for use by subclasses which want to analyze the existing bindings of an object.

## Parameters

- `binding`: The name of a binding.

## See Also

### Managing bindings
- [func valueClassForBinding(NSBindingName) -> AnyClass?](./valueclassforbinding%28_%29.md)
  Returns the class of the value that will be returned for the specified binding.
- [func bind(NSBindingName, to: Any, withKeyPath: String, options: [NSBindingOption : Any]?)](./bind%28_,to,withkeypath,options%29.md)
  Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.
- [func optionDescriptionsForBinding(NSBindingName) -> [NSAttributeDescription]](./optiondescriptionsforbinding%28_%29.md)
  Returns an array describing the options for the specified binding.
- [struct NSBindingInfoKey](../../AppKit/nsbindinginfokey.md)
- [func unbind(NSBindingName)](./unbind%28_%29.md)
  Removes a given binding between the receiver and a controller.
- [func NSIsControllerMarker(Any?) -> Bool](../../AppKit/nsiscontrollermarker%28_%29.md)
  Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/infoforbinding(_:))*