# addMultipartData(_:withName:type:)

**Framework**: Social  
**Kind**: method

Specifies a named multipart POST body for this request.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func addMultipartData(_ data: Data!, withName name: String!, type: String!)
```

#### Discussion

Possible parameter values are dependent on the target service. This information, as well as guidance on when to use a multipart POST body, is documented by the service provider. For links to documentation for the supported services, see Table 1 in [`SLRequest`](slrequest.md).

## Parameters

- `data`: The data for the multipart POST body, such as an image or text.
- `name`: The name of the multipart POST body. This is the name that a specific social service expects.
- `type`: The type of the multipart POST body. This is the MIME content type of the multipart data.

## See Also

- [func addMultipartData(Data!, withName: String!, type: String!, filename: String!)](slrequest/addmultipartdata(_:withname:type:filename:).md)
  Specifies a named multipart POST body for this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequest/addmultipartdata(_:withname:type:))*