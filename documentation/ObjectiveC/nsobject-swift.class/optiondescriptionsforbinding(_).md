# optionDescriptionsForBinding(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns an array describing the options for the specified binding.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func optionDescriptionsForBinding(_ binding: NSBindingName) -> [NSAttributeDescription]
```

```objc
- (NSArray<NSAttributeDescription *> *) optionDescriptionsForBinding:(NSBindingName) binding;
```

#### Return Value

Returns an array of [`NSAttributeDescription`](../../CoreData/nsattributedescription.md) that describe the options for `binding`.

#### Discussion

The [`NSAttributeDescription`](../../CoreData/nsattributedescription.md) instances in the array are used by Interface Builder to build the options editor user interface of the bindings inspector.

- The option name displayed for the option in the bindings inspector is based on the value of the [`NSAttributeDescription`](../../CoreData/nsattributedescription.md) method [`name`](../../CoreData/nspropertydescription/name.md).
- The type of editor displayed for the option in the bindings inspector is based on the value of the  [`NSAttributeDescription`](../../CoreData/nsattributedescription.md) method [`attributeType`](../../CoreData/nsattributedescription/attributetype-swift.property.md).
- The default value displayed in the bindings inspector for the option is based on the value of the [`NSAttributeDescription`](../../CoreData/nsattributedescription.md) method [`defaultValue`](../../CoreData/nsattributedescription/defaultvalue.md).

## Parameters

- `binding`: The name of a binding

## See Also

### Managing bindings
- [func valueClassForBinding(NSBindingName) -> AnyClass?](./valueclassforbinding%28_%29.md)
  Returns the class of the value that will be returned for the specified binding.
- [func bind(NSBindingName, to: Any, withKeyPath: String, options: [NSBindingOption : Any]?)](./bind%28_,to,withkeypath,options%29.md)
  Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.
- [func infoForBinding(NSBindingName) -> [NSBindingInfoKey : Any]?](./infoforbinding%28_%29.md)
  Returns a dictionary describing the receiver’s `binding`.
- [struct NSBindingInfoKey](../../AppKit/nsbindinginfokey.md)
- [func unbind(NSBindingName)](./unbind%28_%29.md)
  Removes a given binding between the receiver and a controller.
- [func NSIsControllerMarker(Any?) -> Bool](../../AppKit/nsiscontrollermarker%28_%29.md)
  Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/optiondescriptionsforbinding(_:))*