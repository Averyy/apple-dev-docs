# optionDescriptionsForBinding(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns an array describing the options for the specified binding.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func optionDescriptionsForBinding(_ binding: NSBindingName) -> [NSAttributeDescription]
```

#### Return Value

Returns an array of [`NSAttributeDescription`](https://developer.apple.com/documentation/coredata/nsattributedescription) that describe the options for `binding`.

#### Discussion

The [`NSAttributeDescription`](https://developer.apple.com/documentation/coredata/nsattributedescription) instances in the array are used by Interface Builder to build the options editor user interface of the bindings inspector.

- The option name displayed for the option in the bindings inspector is based on the value of the [`NSAttributeDescription`](https://developer.apple.com/documentation/coredata/nsattributedescription) method [`name`](https://developer.apple.com/documentation/coredata/nspropertydescription/name).
- The type of editor displayed for the option in the bindings inspector is based on the value of the  [`NSAttributeDescription`](https://developer.apple.com/documentation/coredata/nsattributedescription) method [`attributeType`](https://developer.apple.com/documentation/coredata/nsattributedescription/attributetype-swift.property).
- The default value displayed in the bindings inspector for the option is based on the value of the [`NSAttributeDescription`](https://developer.apple.com/documentation/coredata/nsattributedescription) method [`defaultValue`](https://developer.apple.com/documentation/coredata/nsattributedescription/defaultvalue).

## Parameters

- `binding`: The name of a binding

## See Also

- [func valueClassForBinding(NSBindingName) -> AnyClass?](nsobject-swift.class/valueclassforbinding(_:).md)
  Returns the class of the value that will be returned for the specified binding.
- [func bind(NSBindingName, to: Any, withKeyPath: String, options: [NSBindingOption : Any]?)](nsobject-swift.class/bind(_:to:withkeypath:options:).md)
  Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.
- [func infoForBinding(NSBindingName) -> [NSBindingInfoKey : Any]?](nsobject-swift.class/infoforbinding(_:).md)
  Returns a dictionary describing the receiver’s `binding`.
- [struct NSBindingInfoKey](../appkit/nsbindinginfokey.md)
- [func unbind(NSBindingName)](nsobject-swift.class/unbind(_:).md)
  Removes a given binding between the receiver and a controller.
- [func NSIsControllerMarker(Any?) -> Bool](../appkit/nsiscontrollermarker(_:).md)
  Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/optiondescriptionsforbinding(_:))*