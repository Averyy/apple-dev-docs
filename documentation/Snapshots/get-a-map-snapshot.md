# Create a Maps Web Snapshot

**Framework**: Maps Web Snapshots  
**Kind**: httpRequest

Generates a map image with characteristics that you provide in the query parameters.

**Availability**:
- Maps Web Snapshots 1.0+

## Mentions

- [Generating a URL and Signature to Create a Maps Web Snapshot](generating-a-url-and-signature-to-create-a-maps-web-snapshot.md)

#### Discussion

Use the Snapshot URL query parameters to define characteristics of the map image such as dimensions, language, color scheme, and more.

You must sign every Snapshot URL request and include the signature as the final parameter. For details and example code, see [`Generating a URL and Signature to Create a Maps Web Snapshot`](generating-a-url-and-signature-to-create-a-maps-web-snapshot.md).

## See Also

- [Generating a URL and Signature to Create a Maps Web Snapshot](generating-a-url-and-signature-to-create-a-maps-web-snapshot.md)
  Create a Snapshot URL and generate a signature to validate the request.
- [object Annotation](annotation.md)
  An object for a Snapshot URL that describes annotation characteristics.
- [object Overlay](overlay.md)
  A JSON object for a Snapshot URL that describes overlay shape characteristics, including points for the overlay and styles such as width, color, and dash pattern.
- [object OverlayStyle](overlaystyle.md)
  A  JSON object that describes reusable styles for an overlay.
- [object Image](image.md)
  A JSON object for a Snapshot URL that describes the characteristics of custom images to use for map annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/snapshots/get-a-map-snapshot)*