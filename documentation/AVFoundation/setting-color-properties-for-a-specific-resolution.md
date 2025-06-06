# Setting Color Properties for a Specific Resolution

**Framework**: AVFoundation

Choose the proper color property keys for the desired color range.

#### Overview

After specifying the [`AVVideoColorPropertiesKey`](avvideocolorpropertieskey.md), you must specify a color primary, transfer function, and Y’CbCr matrix.

For HD colorimetry, specify:

- [`AVVideoColorPrimaries_ITU_R_709_2`](avvideocolorprimaries_itu_r_709_2.md)
- [`AVVideoTransferFunction_ITU_R_709_2`](avvideotransferfunction_itu_r_709_2.md)
- [`AVVideoYCbCrMatrix_ITU_R_709_2`](avvideoycbcrmatrix_itu_r_709_2.md)

For SD colorimetry, specify:

- [`AVVideoColorPrimaries_SMPTE_C`](avvideocolorprimaries_smpte_c.md)
- [`AVVideoTransferFunction_ITU_R_709_2`](avvideotransferfunction_itu_r_709_2.md)
- [`AVVideoYCbCrMatrix_ITU_R_601_4`](avvideoycbcrmatrix_itu_r_601_4.md)

For wide gamut HD colorimetry, specify:

- [`AVVideoColorPrimaries_P3_D65`](avvideocolorprimaries_p3_d65.md)
- [`AVVideoTransferFunction_ITU_R_709_2`](avvideotransferfunction_itu_r_709_2.md)
- [`AVVideoYCbCrMatrix_ITU_R_709_2`](avvideoycbcrmatrix_itu_r_709_2.md)

If the source and destination color properties differ, AVFoundation matches the color. You must tag the source.

## See Also

- [let AVVideoAllowWideColorKey: String](avvideoallowwidecolorkey.md)
  The key for a dictionary that indicates whether the client can process wide color.
- [let AVVideoColorPrimariesKey: String](avvideocolorprimarieskey.md)
  The key to identify color primaries in a color properties dictionary.
- [let AVVideoColorPrimaries_EBU_3213: String](avvideocolorprimaries_ebu_3213.md)
  The color primary is in the EBU Tech. 3213 color space.
- [let AVVideoColorPrimaries_ITU_R_2020: String](avvideocolorprimaries_itu_r_2020.md)
  The color primary is in the ITU_R BT.2020 color space for ultra high definition television.
- [let AVVideoColorPrimaries_ITU_R_709_2: String](avvideocolorprimaries_itu_r_709_2.md)
  The color primary is in the ITU_R BT.709 color space.
- [let AVVideoColorPrimaries_P3_D65: String](avvideocolorprimaries_p3_d65.md)
  The color primary uses the DCI-P3 D65 color space.
- [let AVVideoColorPrimaries_SMPTE_C: String](avvideocolorprimaries_smpte_c.md)
  The color primary uses the SMPTE C color space.
- [let AVVideoColorPropertiesKey: String](avvideocolorpropertieskey.md)
  The key for a dictionary that contains properties specifying video color.
- [let AVVideoTransferFunctionKey: String](avvideotransferfunctionkey.md)
  The key to identify the transfer function in a color properties dictionary.
- [let AVVideoTransferFunction_IEC_sRGB: String](avvideotransferfunction_iec_srgb.md)
  The transfer function for the IEC sRGB color space.
- [let AVVideoTransferFunction_ITU_R_2100_HLG: String](avvideotransferfunction_itu_r_2100_hlg.md)
  The transfer function for the ITU_R BT.2100 color space.
- [let AVVideoTransferFunction_ITU_R_709_2: String](avvideotransferfunction_itu_r_709_2.md)
  The transfer function for the ITU_R BT.709 color space.
- [let AVVideoTransferFunction_Linear: String](avvideotransferfunction_linear.md)
  The transfer function for the linear color space.
- [let AVVideoTransferFunction_SMPTE_240M_1995: String](avvideotransferfunction_smpte_240m_1995.md)
  The transfer function for the SMPTE 240M color space.
- [let AVVideoTransferFunction_SMPTE_ST_2084_PQ: String](avvideotransferfunction_smpte_st_2084_pq.md)
  The transfer function for the SMPTE 2084 color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/setting-color-properties-for-a-specific-resolution)*