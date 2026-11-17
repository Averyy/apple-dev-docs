# ar_barcode_detection_symbology_t

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Option set describing possible symbologies of a detected barcode.

**Availability**:
- visionOS

## Declaration

```c
typedef enum { ... } ar_barcode_detection_symbology_t;
```

## Overview

> **Note**: An `ar_barcode_anchor_t` has exactly one symbology. Multiple bits may be set to configure the `ar_barcode_detection_provider_t` to detect multiple symbologies.

## Topics

### Barcode types
- [ar_barcode_detection_symbology_aztec](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_aztec.md)
  Aztec symbology. Decodable at 40 cm distance when greater than 2.0 cm wide.
- [ar_barcode_detection_symbology_codabar](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_codabar.md)
  Codabar symbology. Decodable at 40 cm distance when greater than 5.5 cm wide.
- [ar_barcode_detection_symbology_code_128](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_code_128.md)
  Code 128 symbology. Decodable at 40 cm distance when greater than 2.5 cm wide.
- [ar_barcode_detection_symbology_code_39](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_code_39.md)
  Code 39 symbology. Decodable at 40 cm distance when greater than 6.5 cm wide.
- [ar_barcode_detection_symbology_code_39_checksum](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_code_39_checksum.md)
  Code 39 Checksum symbology. Decodable at 40 cm distance when greater than 6.5 cm wide.
- [ar_barcode_detection_symbology_code_39_full_ascii](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_code_39_full_ascii.md)
  Code 39 Full ASCII symbology. Decodable at 40 cm distance when greater than 3.0 cm wide.
- [ar_barcode_detection_symbology_code_39_full_ascii_checksum](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_code_39_full_ascii_checksum.md)
  Code 39 Full ASCII Checksum symbology. Decodable at 40 cm distance when greater than 4.5 cm wide.
- [ar_barcode_detection_symbology_code_93](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_code_93.md)
  Code 93 symbology. Decodable at 40 cm distance when greater than 5.0 cm wide.
- [ar_barcode_detection_symbology_code_93i](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_code_93i.md)
  Code 93i symbology. Decodable at 40 cm distance when greater than 5.0 cm wide.
- [ar_barcode_detection_symbology_data_matrix](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_data_matrix.md)
  Data Matrix symbology. Decodable at 40 cm distance when greater than 1.0 cm wide.
- [ar_barcode_detection_symbology_ean_13](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_ean_13.md)
  EAN-13 symbology. Decodable at 40 cm distance when greater than 4.0 cm wide.
- [ar_barcode_detection_symbology_ean_8](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_ean_8.md)
  EAN-8 symbology. Decodable at 40 cm distance when greater than 3.0 cm wide.
- [ar_barcode_detection_symbology_gs1_databar](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_gs1_databar.md)
  GS1 Databar symbology. Decodable at 40 cm distance when greater than 3.0 cm wide.
- [ar_barcode_detection_symbology_gs1_databar_expanded](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_gs1_databar_expanded.md)
  GS1 Databar Expanded symbology. Decodable at 40 cm distance when greater than 6.5 cm wide.
- [ar_barcode_detection_symbology_gs1_databar_limited](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_gs1_databar_limited.md)
  GS1 Databar Limited symbology. Decodable at 40 cm distance when greater than 3.0 cm wide.
- [ar_barcode_detection_symbology_itf](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_itf.md)
  ITF symbology. Decodable at 40 cm distance when greater than 3.5 cm wide.
- [ar_barcode_detection_symbology_itf_14](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_itf_14.md)
  ITF-14 symbology. Decodable at 40 cm distance when greater than 5.0 cm wide.
- [ar_barcode_detection_symbology_itf_checksum](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_itf_checksum.md)
  ITF Checksum symbology. Decodable at 40 cm distance when greater than 3.5 cm wide.
- [ar_barcode_detection_symbology_micropdf417](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_micropdf417.md)
  MicroPDF417 symbology. Decodable at 40 cm distance when greater than 6.5 cm wide.
- [ar_barcode_detection_symbology_microqr](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_microqr.md)
  MicroQR symbology. Decodable at 40 cm distance when greater than 2.0 cm wide.
- [ar_barcode_detection_symbology_msi_plessey](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_msi_plessey.md)
  MSIPlessey symbology. Decodable at 40 cm distance when greater than 4.5 cm wide.
- [ar_barcode_detection_symbology_none](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_none.md)
  Option set describing possible symbologies of a detected barcode.
- [ar_barcode_detection_symbology_pdf417](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_pdf417.md)
  PDF417 symbology. Decodable at 40 cm distance when greater than 6.0 cm wide.
- [ar_barcode_detection_symbology_qr](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_qr.md)
  QR symbology. Decodable at 40 cm distance when greater than 1.5 cm wide.
- [ar_barcode_detection_symbology_upce](./ar_barcode_detection_symbology_t/ar_barcode_detection_symbology_upce.md)
  UPC-E symbology. Decodable at 40 cm distance when greater than 2.5 cm wide.

## See Also

### Barcode functions
- [ar_barcode_anchor_copy_payload_data](./ar_barcode_anchor_copy_payload_data.md)
  Get a copy of a barcode anchor’s payload data.
- [ar_barcode_anchor_get_extent](./ar_barcode_anchor_get_extent.md)
  Get the extent of a detected barcode’s bounding box.
- [ar_barcode_anchor_get_identifier](./ar_barcode_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_barcode_anchor_get_origin_from_anchor_transform](./ar_barcode_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_barcode_anchor_get_payload_string_value](./ar_barcode_anchor_get_payload_string_value.md)
  Get the payload string value of a barcode anchor.
- [ar_barcode_anchor_get_symbology](./ar_barcode_anchor_get_symbology.md)
  Get the symbology of a barcode anchor.
- [ar_barcode_anchor_get_timestamp](./ar_barcode_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_barcode_anchors_enumerate_anchors](./ar_barcode_anchors_enumerate_anchors.md)
  Enumerate a collection of barcode anchors.
- [ar_barcode_anchors_enumerate_anchors_f](./ar_barcode_anchors_enumerate_anchors_f.md)
  Enumerates a collection of barcode anchors using a function.
- [ar_barcode_anchors_get_count](./ar_barcode_anchors_get_count.md)
  Get the count of barcode anchors in a collection.
- [ar_barcode_detection_configuration_create](./ar_barcode_detection_configuration_create.md)
  Create a barcode detection configuration.
- [ar_barcode_detection_configuration_set_detection_symbology](./ar_barcode_detection_configuration_set_detection_symbology.md)
  Set the desired symbologies to detect.
- [ar_barcode_detection_provider_create](./ar_barcode_detection_provider_create.md)
  Create a barcode detection provider.
- [ar_barcode_detection_provider_get_required_authorization_type](./ar_barcode_detection_provider_get_required_authorization_type.md)
  Get the authorization type required by the barcode detection provider.
- [ar_barcode_detection_provider_is_supported](./ar_barcode_detection_provider_is_supported.md)
  Determines whether this device supports the barcode detection provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_barcode_detection_symbology_t)*