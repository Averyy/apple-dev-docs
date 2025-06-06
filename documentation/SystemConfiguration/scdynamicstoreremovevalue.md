# SCDynamicStoreRemoveValue(_:_:)

**Framework**: System Configuration  
**Kind**: func

Removes the value of the specified key from the dynamic store.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreRemoveValue(_ store: SCDynamicStore?, _ key: CFString) -> Bool
```

#### Return Value

`TRUE` if the key was removed; `FALSE` if no value was located or an error occurred.

## Parameters

- `store`: The dynamic store session.
- `key`: The key of the value to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstoreremovevalue(_:_:))*