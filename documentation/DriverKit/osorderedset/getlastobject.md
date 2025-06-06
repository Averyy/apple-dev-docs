# getLastObject

**Framework**: DriverKit  
**Kind**: method

The last object in the ordered set if there is one, otherwise `NULL`.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
OSObject * getLastObject() const;
```

#### Discussion

The returned object will be released if removed from the ordered set; if you plan to store the reference, you should call retain on that object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osorderedset/getlastobject)*