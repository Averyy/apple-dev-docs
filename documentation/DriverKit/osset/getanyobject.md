# getAnyObject

**Framework**: DriverKit  
**Kind**: method

Returns an arbitrary (not random) object from the set.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
OSObject * getAnyObject() const;
```

#### Return Value

An arbitrary (not random) object if one exists within the set.

#### Discussion

The returned object will be released if removed from the set; if you plan to store the reference, you should call retain on that object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osset/getanyobject)*