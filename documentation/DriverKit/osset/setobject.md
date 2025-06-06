# setObject

**Framework**: DriverKit  
**Kind**: method

Adds an object to the OSSet if it is not already present.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool setObject(const OSMetaClassBase * anObject);
```

#### Return Value

`true` if `anObject` was successfully added to the set, `false` otherwise (including if it was already in the set).

#### Discussion

The set adds storage to accomodate the new object, if necessary. If successfully added, the object is retained.

A `false` return value can mean either that `anObject` is already present in the set, or that a memory allocation failure occurred. If you need to know whether the object is already present, use containsObject.

## Parameters

- `anObject`: The OSMetaClassBase-derived object to be added to the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osset/setobject)*