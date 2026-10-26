# Numbers, Data, and Basic Values

**Framework**: Foundation  
**Role**: API Collection

Work with primitive values and other fundamental types used throughout Cocoa.

## Topics

### Numbers
- [struct Int](../Swift/int.md)
  A signed integer value type.
- [struct Double](../Swift/double.md)
  A double-precision (64-bit), floating-point value type.
- [struct Decimal](./decimal.md)
  A structure representing a base-10 number.
- [class NumberFormatter](./numberformatter.md)
  A formatter that converts between numeric values and their textual representations.
- [NSInteger](../ObjectiveC/nsinteger.md)
  Describes an integer.
- [NSUInteger](../ObjectiveC/nsuinteger.md)
  Describes an unsigned integer.
- [NSDecimalNumber](./nsdecimalnumber.md)
  An object for representing and performing arithmetic on base-10 numbers.
- [NSNumber](./nsnumber.md)
  An object wrapper for primitive scalar numeric values.
### Binary Data
- [struct Data](./data.md)
  A byte buffer in memory.
- [protocol DataProtocol](./dataprotocol.md)
  A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous data buffers.
- [protocol MutableDataProtocol](./mutabledataprotocol.md)
  A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous mutable data buffers.
- [protocol ContiguousBytes](./contiguousbytes.md)
  A protocol that declares the type offers direct access to the underlying raw bytes in a contiguous manner.
- [NSData](./nsdata.md)
  A static byte buffer in memory.
- [NSMutableData](./nsmutabledata.md)
  An object representing a dynamic byte buffer in memory.
### URLs
- [struct URL](./url.md)
  A value that identifies the location of a resource, such as an item on a remote server or the path to a local file.
- [struct URLComponents](./urlcomponents.md)
  A structure that parses URLs into and constructs URLs from their constituent parts.
- [struct URLQueryItem](./urlqueryitem.md)
  A single name-value pair from the query portion of a URL.
- [NSURL](./nsurl.md)
  An object that represents the location of a resource, such as an item on a remote server or the path to a local file.
- [NSURLComponents](./nsurlcomponents.md)
  An object that parses URLs into and constructs URLs from their constituent parts.
- [NSURLQueryItem](./nsurlqueryitem.md)
  An object representing a single name/value pair for an item in the query portion of a URL.
### Unique Identifiers
- [struct UUID](./uuid.md)
  A universally unique value to identify types, interfaces, and other items.
- [NSUUID](./nsuuid.md)
  A universally unique value that can be used to identify types, interfaces, and other items.
### Geometry
- [struct CGFloat](../CoreFoundation/cgfloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [typealias NSPoint](./nspoint.md)
  A point in a Cartesian coordinate system.
- [typealias NSSize](./nssize.md)
  A two-dimensional size.
- [typealias NSRect](./nsrect.md)
  A rectangle.
- [struct AffineTransform](./affinetransform.md)
  A graphics coordinate transformation.
- [struct NSEdgeInsets](./nsedgeinsets.md)
  A description of the distance between the edges of two rectangles.
- [NSAffineTransform](./nsaffinetransform.md)
  A graphics coordinate transformation.
### Ranges
- [typealias NSRange](./nsrange-swift.typealias.md)
  A structure used to describe a portion of a series, such as characters in a string or objects in an array.
- [NSRange](./nsrange-c.struct.md)
  A structure used to describe a portion of a series, such as characters in a string or objects in an array.

## See Also

### Fundamentals
- [Strings and Text](./strings-and-text.md)
  Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](./collections.md)
  Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](./dates-and-times.md)
  Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](./units-and-measurement.md)
  Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](./data-formatting.md)
  Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](./filters-and-sorting.md)
  Use predicates, expressions, and sort descriptors to examine elements in collections and other services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numbers-data-and-basic-values)*