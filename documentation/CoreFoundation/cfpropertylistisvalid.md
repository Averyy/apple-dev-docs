# CFPropertyListIsValid(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Determines if a property list is valid.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFPropertyListIsValid(_ plist: CFPropertyList!, _ format: CFPropertyListFormat) -> Bool
```

#### Return Value

`true` if the object graph rooted at `plist` is a valid property list graph—that is, the property list contains no cycles, only contains property list objects, and all dictionary keys are strings; otherwise `false`.

#### Discussion

The debugging library version of this function prints out some useful messages.

## Parameters

- `plist`: The property list to validate.
- `format`: A constant that specifies the allowable format of  . See   for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistisvalid(_:_:))*