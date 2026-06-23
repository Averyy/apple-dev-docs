# InsertData

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
virtual kern_return_t InsertData(OSData *data);
```

#### Return Value

0 in case of success. Negative in case of an error.

#### Discussion

This function is called to insert data into the buffer.

This function overwrites the data in the buffer. The write starts from offset 0 and continues until ‘len’

## Parameters

- `data`: Data to be inserted


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioextensiblepaniclog/insertdata)*