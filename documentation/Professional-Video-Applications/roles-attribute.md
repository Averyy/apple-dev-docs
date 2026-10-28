# Roles Attribute

**Framework**: Professional-Video-Applications  
**Role**: Article

Assign video, audio, title, and caption elements a role.

## Overview

You can assign a role to a media component to distinguish the nature of the media component from other components. The `role` attribute format is: `main-role.sub-role`.

For captions, the main role must include the caption format in the following form: *roleName?*`captionFormat=`*captionFormat*.

The subrole must reflect the particular language tag, and optional region tag, for the caption role, for example, `en` or `en-US`. The following table provides details on these values.

| Component | Description |
| --- | --- |
| `roleName` | The caption role name. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) *Cannot contain the “.” or “?” characters.* ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) *Cannot be only an “_” character.* ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) **Note:** Users can edit the caption role name in the Role Editor. |
| `captionFormat` | The caption format. Valid values are `ITT` or `CEA608`. |
| `sub-role` | The language tag, and optional region tag, for the subrole. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) Final Cut Pro supports only a subset of language tags. Final Cut Pro automatically maps unsupported language tags to `en` (English). ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) Final Cut Pro formats language codes according to RFC 5646, which is a part of BCP 47. |

The following are caption role examples:

- `”ITT Subtitles?captionFormat=ITT.en”`: The English language subrole of an ITT format caption role named `ITT Subtitles`.
- `”My Subtitles?captionFormat=ITT.fr-CA”`: The French (Canada) language subrole of an ITT format caption role named `My Subtitles`.
- `”CEA-608 Captions?captionFormat=CEA608.it”`: The Italian language subrole of a CEA608 format caption role named `CEA-608 Captions`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/roles-attribute)*