# bind(_:to:withKeyPath:options:)

**Framework**: Objective-C Runtime  
**Kind**: method

Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.

**Availability**:
- macOS ?+

## Declaration

```swift
func bind(_ binding: NSBindingName, to observable: Any, withKeyPath keyPath: String, options: [NSBindingOption : Any]? = nil)
```

## Parameters

- `binding`: The key path for a property of the receiver previously exposed using the [`exposeBinding(_:)`](nsobject-swift.class/exposebinding(_:).md) method.
- `observable`: The bound-to object.
- `keyPath`: A key path to a property reachable from `observableController`. The elements in the path must be key-value observing compliant (see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i)).
- `options`: A dictionary containing options for the binding, such as placeholder objects or an `NSValueTransformer` identifier as described in Constants. This value is optional—pass `nil` to specify no options.

## See Also

- [func valueClassForBinding(NSBindingName) -> AnyClass?](nsobject-swift.class/valueclassforbinding(_:).md)
  Returns the class of the value that will be returned for the specified binding.
- [func optionDescriptionsForBinding(NSBindingName) -> [NSAttributeDescription]](nsobject-swift.class/optiondescriptionsforbinding(_:).md)
  Returns an array describing the options for the specified binding.
- [func infoForBinding(NSBindingName) -> [NSBindingInfoKey : Any]?](nsobject-swift.class/infoforbinding(_:).md)
  Returns a dictionary describing the receiver’s `binding`.
- [struct NSBindingInfoKey](../appkit/nsbindinginfokey.md)
- [func unbind(NSBindingName)](nsobject-swift.class/unbind(_:).md)
  Removes a given binding between the receiver and a controller.
- [func NSIsControllerMarker(Any?) -> Bool](../appkit/nsiscontrollermarker(_:).md)
  Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/bind(_:to:withkeypath:options:))*