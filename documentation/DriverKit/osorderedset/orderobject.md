# orderObject

**Framework**: DriverKit  
**Kind**: method

Calls the ordered set’s order function against a `NULL` object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
int32_t orderObject(const OSMetaClassBase * anObject);
```

#### Return Value

The ordering value for the object.

#### Discussion

This function calls the ordered set’s order function with `anObject`, `NULL`, and the ordering context (or `NULL` if none was set), and returns the result of that function.

## Parameters

- `anObject`: The object to be ordered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osorderedset/orderobject)*