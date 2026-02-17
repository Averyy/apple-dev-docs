# init

**Framework**: NetworkingDriverKit  
**Kind**: method

Initializes the network packet object.

**Availability**:
- DriverKit ?+

## Declaration

```swift
virtual bool init();
```

#### Return Value

`YES` if initialization was successful, or `NO` if it wasn’t.

#### Discussion

Do not call this method directly. Submission queues initialize packets before returning them to your driver to process.

## See Also

- [free](iousernetworkpacket/free.md)
  Performs any final cleanup for the network packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/init)*