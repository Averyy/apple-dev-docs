# operator=

**Framework**: DriverKit  
**Kind**: method  
**Role**: Method Template

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
template <typename U, typename = std::std::enable_if_t<std::is_convertible_v<U *, T *>>> OSSharedPtr<T> & operator=(OSSharedPtr<U> && other);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ossharedptr/operator=-lttt)*