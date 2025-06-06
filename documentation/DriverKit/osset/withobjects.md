# withObjects

**Framework**: DriverKit  
**Kind**: method

Creates and initializes an OSSet populated with objects provided.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSSetPtr withObjects(const OSObject * * values, uint32_t count, uint32_t capacity);
```

#### Return Value

An instance of OSSet containing the objects provided, with a retain count of 1; `NULL` on failure.

#### Discussion

`objects` must be non-`NULL`, and `count` must be nonzero. If `capacity` is nonzero, it must be greater than or equal to `count`. The new OSSet will grow as needed to accommodate more objects ([`CFMutableSet`](https://developer.apple.com/documentation/CoreFoundation/CFMutableSet), for which the initial capacity is a hard limit).

The objects in `objects` are retained for storage in the new set, not copied.

## Parameters

- `values`: A C array of OSMetaClassBase-derived objects.
- `count`: The number of objects to be placed into the set.
- `capacity`: The initial storage capacity of the new set object. If 0,   is used; otherwise this value must be greater than or equal to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osset/withobjects)*