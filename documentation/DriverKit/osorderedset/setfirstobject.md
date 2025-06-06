# setFirstObject

**Framework**: DriverKit  
**Kind**: method

Adds an object to the OSOrderedSet at index 0 if it is not already present.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool setFirstObject(const OSMetaClassBase * anObject);
```

#### Return Value

`true` if `anObject` was successfully added to the ordered set, `false` otherwise (including if it was already in the ordered set at any index).

#### Discussion

The set adds storage to accomodate the new object, if necessary. If successfully added, the object is retained.

This function ignores any ordering function of the ordered set, and can disrupt the automatic sorting mechanism. Only call this function if you are managing the ordered set directly.

A `false` return value can mean either that `anObject` is already present in the set, or that a memory allocation failure occurred. If you need to know whether the object is already present, use containsObject(const OSMetaClassBase *).

## Parameters

- `anObject`: The OSMetaClassBase-derived object to be added to the ordered set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osorderedset/setfirstobject)*