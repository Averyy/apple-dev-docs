# getContainer

**Framework**: CloudKit JS  
**Kind**: method

Returns the container with the specified container ID.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
CloudKit.Container getContainer(
	String containerIdentifier
);
```

#### Return Value

The container with the specified container ID if it exists; otherwise, the value is undefined.

## Parameters

- `containerIdentifier`: The identifier for the container you want to get.

## See Also

- [getDefaultContainer](cloudkit/getdefaultcontainer.md)
  Returns the default container.
- [getAllContainers](cloudkit/getallcontainers.md)
  Returns all the containers that were configured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit/getcontainer)*