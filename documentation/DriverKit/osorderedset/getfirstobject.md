# getFirstObject

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

The object at index 0 in the ordered set if there is one, otherwise `NULL`.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
OSObject * getFirstObject() const;
```

#### Discussion

The returned object will be released if removed from the ordered set; if you plan to store the reference, you should call retain on that object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osorderedset/getfirstobject)*