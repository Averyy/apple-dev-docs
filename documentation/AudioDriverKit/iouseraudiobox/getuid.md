# GetUID

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the UID of the audio box.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
OSSharedPtr<OSString> GetUID();
```

#### Return Value

The UID of the audio box.

#### Discussion

This method synchronizes by using the work queue created by the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/getuid)*