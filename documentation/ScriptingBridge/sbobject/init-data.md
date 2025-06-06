# init(data:)

**Framework**: Scripting Bridge  
**Kind**: init

Returns an instance of an `SBObject` subclass initialized with the given data.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
init(data: Any)
```

#### Return Value

An `SBObject` object or `nil` if the object could not be initialized.

#### Discussion

Scripting Bridge does not actually create an object in the target application until you add the object returned from this method to an element array ([`SBElementArray`](sbelementarray.md)).

## Parameters

- `data`: An object containing data for the new   object. The data   varies according to the type of scripting object to be created.

## See Also

- [init()](sbobject/init.md)
  Initializes and returns an instance of an `SBObject` subclass.
- [init(properties: [AnyHashable : Any])](sbobject/init(properties:).md)
  Returns an instance of an `SBObject` subclass initialized with the specified properties.
- [init(elementCode: DescType, properties: [String : Any]?, data: Any?)](sbobject/init(elementcode:properties:data:).md)
  Returns an instance of an `SBObject` subclass initialized with the specified properties and data and added to the designated element array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/init(data:))*