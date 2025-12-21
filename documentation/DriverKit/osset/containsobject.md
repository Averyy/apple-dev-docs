# containsObject

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool containsObject(const OSMetaClassBase * anObject) const;
```

#### Return Value

If anObject is non-NULL and present within the set, false otherwise.

#### Discussion

Checks the set for the presence of an object.

Checks the set for the presence of an object.

## Parameters

- `anObject`: The OSMetaClassBase-derived object to check for in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osset/containsobject)*