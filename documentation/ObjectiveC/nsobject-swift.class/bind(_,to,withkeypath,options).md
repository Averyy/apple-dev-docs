# bind(_:to:withKeyPath:options:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.

**Availability**:
- macOS

## Declaration

```swift
func bind(_ binding: NSBindingName, to observable: Any, withKeyPath keyPath: String, options: [NSBindingOption : Any]? = nil)
```

```objc
- (void) bind:(NSBindingName) binding toObject:(id) observable withKeyPath:(NSString *) keyPath options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `binding`: The key path for a property of the receiver previously exposed using the [`exposeBinding(_:)`](./exposebinding%28_%29.md) method.
- `observable`: The bound-to object.
- `keyPath`: A key path to a property reachable from `observableController`. The elements in the path must be key-value observing compliant (see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i)).
- `options`: A dictionary containing options for the binding, such as placeholder objects or an `NSValueTransformer` identifier as described in Constants. This value is optional—pass `nil` to specify no options.

## See Also

### Managing bindings
- [func valueClassForBinding(NSBindingName) -> AnyClass?](./valueclassforbinding%28_%29.md)
  Returns the class of the value that will be returned for the specified binding.
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/bind(_:to:withkeypath:options:))*