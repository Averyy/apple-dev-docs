# Numbers, Data, and Basic Values

**Framework**: Foundation

Work with primitive values and other fundamental types used throughout Cocoa.

## Topics

### Numbers
- [@frozen struct Int](../Swift/Int.md)
  A signed integer value type.
- [@frozen struct Double](../Swift/Double.md)
  A double-precision, floating-point value type.
- [struct Decimal](decimal.md)
  A structure representing a base-10 number.
- [class NumberFormatter](numberformatter.md)
  A formatter that converts between numeric values and their textual representations.
### Binary Data
- [struct Data](data.md)
  A byte buffer in memory.
- [protocol DataProtocol](dataprotocol.md)
  A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous data buffers.
- [protocol MutableDataProtocol](mutabledataprotocol.md)
  A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous mutable data buffers.
- [protocol ContiguousBytes](contiguousbytes.md)
  A protocol that declares the type offers direct access to the underlying raw bytes in a contiguous manner.
### URLs
- [struct URL](url.md)
  A value that identifies the location of a resource, such as an item on a remote server or the path to a local file.
- [struct URLComponents](urlcomponents.md)
  A structure that parses URLs into and constructs URLs from their constituent parts.
- [struct URLQueryItem](urlqueryitem.md)
  A single name-value pair from the query portion of a URL.
### Unique Identifiers
- [struct UUID](uuid.md)
  A universally unique value to identify types, interfaces, and other items.
### Geometry
- [@frozen struct CGFloat](../CoreFoundation/CGFloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [typealias NSPoint](nspoint.md)
  A point in a Cartesian coordinate system.
- [typealias NSSize](nssize.md)
  A two-dimensional size.
- [typealias NSRect](nsrect.md)
  A rectangle.
- [struct AffineTransform](affinetransform.md)
  A graphics coordinate transformation.
- [struct NSEdgeInsets](nsedgeinsets.md)
  A description of the distance between the edges of two rectangles.
### Ranges
- [typealias NSRange](nsrange.md)
  A structure used to describe a portion of a series, such as characters in a string or objects in an array.

## See Also

- [Strings and Text](strings-and-text.md)
  Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](collections.md)
  Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](dates-and-times.md)
  Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](units-and-measurement.md)
  Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](data-formatting.md)
  Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](filters-and-sorting.md)
  Use predicates, expressions, and sort descriptors to examine elements in collections and other services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numbers-data-and-basic-values)*