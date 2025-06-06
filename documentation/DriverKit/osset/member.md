# member

**Framework**: DriverKit  
**Kind**: method

Checks the set for the presence of an object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool member(const OSMetaClassBase * anObject) const;
```

#### Return Value

`true` if `anObject` is present within the set, `false` otherwise.

#### Discussion

Pointer equality is used. This function returns `false` if passed `NULL`.

containsObject checks for `NULL` first, and is therefore more efficient than this function.

## Parameters

- `anObject`: The OSMetaClassBase-derived object to check for in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osset/member)*