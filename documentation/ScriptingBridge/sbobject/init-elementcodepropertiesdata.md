# init(elementCode:properties:data:)

**Framework**: Scripting Bridge  
**Kind**: init

Returns an instance of an `SBObject` subclass initialized with the specified properties and data and added to the designated element array.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
init(elementCode code: DescType, properties: [String : Any]?, data: Any?)
```

#### Return Value

An `SBObject` object or `nil` if the object could not be initialized.

#### Discussion

Unlike the other initializers of this class, this method not only initializes the `SBObject` object but adds it to a specified element array. This method is the designated initializer.

## Parameters

- `code`: A four-character code used to identify an element in the target   application’s scripting interface. See     for details.
- `properties`: A dictionary with   keys specifying the four-character codes of properties   (that is, attributes or to-one relationships) and the values for those   properties. Pass   if you are initializing the object by   only.
- `data`: An object containing data for the new   object. The data   varies according to the type of scripting object to be created. Pass    if you initializing the object by   only.

## See Also

- [init()](sbobject/init.md)
  Initializes and returns an instance of an `SBObject` subclass.
- [init(data: Any)](sbobject/init(data:).md)
  Returns an instance of an `SBObject` subclass initialized with the given data.
- [init(properties: [AnyHashable : Any])](sbobject/init(properties:).md)
  Returns an instance of an `SBObject` subclass initialized with the specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/init(elementcode:properties:data:))*