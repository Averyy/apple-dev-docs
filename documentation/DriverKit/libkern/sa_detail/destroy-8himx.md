# destroy

**Framework**: DriverKit  
**Kind**: func  
**Role**: Function Template

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
template <typename T, enable_if_t<is_trivially_destructible_v<T>> * = nullptr> void destroy(T * *, T * *);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/libkern/sa_detail/destroy-8himx)*