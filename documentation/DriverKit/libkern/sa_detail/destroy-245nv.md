# destroy

**Framework**: DriverKit  
**Kind**: func

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
template <typename T, enable_if_t<!is_trivially_destructible_v<T>> * = nullptr> void destroy(T * * first, T * * last);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/libkern/sa_detail/destroy-245nv)*