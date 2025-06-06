# operator=

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
template <typename U, typename = std::std::enable_if_t<std::is_convertible_v<U *, T *>>> OSSharedPtr<T> & operator=(const OSSharedPtr<U> & other);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ossharedptr/operator=-5z7no)*