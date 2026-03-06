# Get All Storefronts

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch all the storefronts in alphabetical order.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains one or more [`Storefronts`](storefronts.md) objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

##### Example

**Request**:

```None
https://api.music.apple.com/v1/storefronts
```

**Response**:

```json
{
    "data": [
        {
            "id": "dz",
            "type": "storefronts",
            "href": "/v1/storefronts/dz",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Algeria",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR",
                    "ar"
                ]
            }
        },
        {
            "id": "ao",
            "type": "storefronts",
            "href": "/v1/storefronts/ao",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Angola",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "ai",
            "type": "storefronts",
            "href": "/v1/storefronts/ai",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Anguilla",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "ag",
            "type": "storefronts",
            "href": "/v1/storefronts/ag",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Antigua and Barbuda",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "ar",
            "type": "storefronts",
            "href": "/v1/storefronts/ar",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Argentina",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "am",
            "type": "storefronts",
            "href": "/v1/storefronts/am",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Armenia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "au",
            "type": "storefronts",
            "href": "/v1/storefronts/au",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Australia",
                "defaultLanguageTag": "en-AU",
                "supportedLanguageTags": [
                    "en-AU",
                    "en-GB"
                ]
            }
        },
        {
            "id": "at",
            "type": "storefronts",
            "href": "/v1/storefronts/at",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Austria",
                "defaultLanguageTag": "de-DE",
                "supportedLanguageTags": [
                    "de-DE",
                    "en-GB"
                ]
            }
        },
        {
            "id": "az",
            "type": "storefronts",
            "href": "/v1/storefronts/az",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Azerbaijan",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "bs",
            "type": "storefronts",
            "href": "/v1/storefronts/bs",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Bahamas",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "bh",
            "type": "storefronts",
            "href": "/v1/storefronts/bh",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Bahrain",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ar"
                ]
            }
        },
        {
            "id": "bb",
            "type": "storefronts",
            "href": "/v1/storefronts/bb",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Barbados",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "by",
            "type": "storefronts",
            "href": "/v1/storefronts/by",
            "attributes": {
                "explicitContentPolicy": "prohibited",
                "name": "Belarus",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "be",
            "type": "storefronts",
            "href": "/v1/storefronts/be",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Belgium",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR",
                    "nl"
                ]
            }
        },
        {
            "id": "bz",
            "type": "storefronts",
            "href": "/v1/storefronts/bz",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Belize",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "es-MX"
                ]
            }
        },
        {
            "id": "bj",
            "type": "storefronts",
            "href": "/v1/storefronts/bj",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Benin",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "bm",
            "type": "storefronts",
            "href": "/v1/storefronts/bm",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Bermuda",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "bt",
            "type": "storefronts",
            "href": "/v1/storefronts/bt",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Bhutan",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "bo",
            "type": "storefronts",
            "href": "/v1/storefronts/bo",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Bolivia",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "ba",
            "type": "storefronts",
            "href": "/v1/storefronts/ba",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Bosnia and Herzegovina",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "hr"
                ]
            }
        },
        {
            "id": "bw",
            "type": "storefronts",
            "href": "/v1/storefronts/bw",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Botswana",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "br",
            "type": "storefronts",
            "href": "/v1/storefronts/br",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Brazil",
                "defaultLanguageTag": "pt-BR",
                "supportedLanguageTags": [
                    "pt-BR",
                    "en-GB"
                ]
            }
        },
        {
            "id": "vg",
            "type": "storefronts",
            "href": "/v1/storefronts/vg",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "British Virgin Islands",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "bg",
            "type": "storefronts",
            "href": "/v1/storefronts/bg",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Bulgaria",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "kh",
            "type": "storefronts",
            "href": "/v1/storefronts/kh",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Cambodia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "cm",
            "type": "storefronts",
            "href": "/v1/storefronts/cm",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Cameroon",
                "defaultLanguageTag": "fr-FR",
                "supportedLanguageTags": [
                    "fr-FR",
                    "en-GB"
                ]
            }
        },
        {
            "id": "ca",
            "type": "storefronts",
            "href": "/v1/storefronts/ca",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Canada",
                "defaultLanguageTag": "en-CA",
                "supportedLanguageTags": [
                    "en-CA",
                    "fr-CA"
                ]
            }
        },
        {
            "id": "cv",
            "type": "storefronts",
            "href": "/v1/storefronts/cv",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Cape Verde",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "ky",
            "type": "storefronts",
            "href": "/v1/storefronts/ky",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Cayman Islands",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "td",
            "type": "storefronts",
            "href": "/v1/storefronts/td",
            "attributes": {
                "explicitContentPolicy": "prohibited",
                "name": "Chad",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "cl",
            "type": "storefronts",
            "href": "/v1/storefronts/cl",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Chile",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "cn",
            "type": "storefronts",
            "href": "/v1/storefronts/cn",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "China mainland",
                "defaultLanguageTag": "zh-Hans-CN",
                "supportedLanguageTags": [
                    "zh-Hans-CN",
                    "en-GB"
                ]
            }
        },
        {
            "id": "co",
            "type": "storefronts",
            "href": "/v1/storefronts/co",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Colombia",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "cr",
            "type": "storefronts",
            "href": "/v1/storefronts/cr",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Costa Rica",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "hr",
            "type": "storefronts",
            "href": "/v1/storefronts/hr",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Croatia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "hr"
                ]
            }
        },
        {
            "id": "cy",
            "type": "storefronts",
            "href": "/v1/storefronts/cy",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Cyprus",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "el",
                    "tr"
                ]
            }
        },
        {
            "id": "cz",
            "type": "storefronts",
            "href": "/v1/storefronts/cz",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Czech Republic",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "cs"
                ]
            }
        },
        {
            "id": "ci",
            "type": "storefronts",
            "href": "/v1/storefronts/ci",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Côte d’Ivoire",
                "defaultLanguageTag": "fr-FR",
                "supportedLanguageTags": [
                    "fr-FR",
                    "en-GB"
                ]
            }
        },
        {
            "id": "cd",
            "type": "storefronts",
            "href": "/v1/storefronts/cd",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Democratic Republic of the Congo",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "dk",
            "type": "storefronts",
            "href": "/v1/storefronts/dk",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Denmark",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "da"
                ]
            }
        },
        {
            "id": "dm",
            "type": "storefronts",
            "href": "/v1/storefronts/dm",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Dominica",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "do",
            "type": "storefronts",
            "href": "/v1/storefronts/do",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Dominican Republic",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "ec",
            "type": "storefronts",
            "href": "/v1/storefronts/ec",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Ecuador",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "eg",
            "type": "storefronts",
            "href": "/v1/storefronts/eg",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Egypt",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR",
                    "ar"
                ]
            }
        },
        {
            "id": "sv",
            "type": "storefronts",
            "href": "/v1/storefronts/sv",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "El Salvador",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "ee",
            "type": "storefronts",
            "href": "/v1/storefronts/ee",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Estonia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "sz",
            "type": "storefronts",
            "href": "/v1/storefronts/sz",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Eswatini",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "fj",
            "type": "storefronts",
            "href": "/v1/storefronts/fj",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Fiji",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "fi",
            "type": "storefronts",
            "href": "/v1/storefronts/fi",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Finland",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fi"
                ]
            }
        },
        {
            "id": "fr",
            "type": "storefronts",
            "href": "/v1/storefronts/fr",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "France",
                "defaultLanguageTag": "fr-FR",
                "supportedLanguageTags": [
                    "fr-FR",
                    "en-GB"
                ]
            }
        },
        {
            "id": "ga",
            "type": "storefronts",
            "href": "/v1/storefronts/ga",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Gabon",
                "defaultLanguageTag": "fr-FR",
                "supportedLanguageTags": [
                    "fr-FR",
                    "en-GB"
                ]
            }
        },
        {
            "id": "gm",
            "type": "storefronts",
            "href": "/v1/storefronts/gm",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Gambia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "ge",
            "type": "storefronts",
            "href": "/v1/storefronts/ge",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Georgia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "de",
            "type": "storefronts",
            "href": "/v1/storefronts/de",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Germany",
                "defaultLanguageTag": "de-DE",
                "supportedLanguageTags": [
                    "de-DE",
                    "en-GB"
                ]
            }
        },
        {
            "id": "gh",
            "type": "storefronts",
            "href": "/v1/storefronts/gh",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Ghana",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "gr",
            "type": "storefronts",
            "href": "/v1/storefronts/gr",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Greece",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "el"
                ]
            }
        },
        {
            "id": "gd",
            "type": "storefronts",
            "href": "/v1/storefronts/gd",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Grenada",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "gt",
            "type": "storefronts",
            "href": "/v1/storefronts/gt",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Guatemala",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "gw",
            "type": "storefronts",
            "href": "/v1/storefronts/gw",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Guinea-Bissau",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "gy",
            "type": "storefronts",
            "href": "/v1/storefronts/gy",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Guyana",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "hn",
            "type": "storefronts",
            "href": "/v1/storefronts/hn",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Honduras",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "hk",
            "type": "storefronts",
            "href": "/v1/storefronts/hk",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Hong Kong",
                "defaultLanguageTag": "zh-Hant-HK",
                "supportedLanguageTags": [
                    "zh-Hant-HK",
                    "en-GB",
                    "zh-Hant-TW"
                ]
            }
        },
        {
            "id": "hu",
            "type": "storefronts",
            "href": "/v1/storefronts/hu",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Hungary",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "hu"
                ]
            }
        },
        {
            "id": "is",
            "type": "storefronts",
            "href": "/v1/storefronts/is",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Iceland",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "in",
            "type": "storefronts",
            "href": "/v1/storefronts/in",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "India",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "hi"
                ]
            }
        },
        {
            "id": "id",
            "type": "storefronts",
            "href": "/v1/storefronts/id",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Indonesia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "id"
                ]
            }
        },
        {
            "id": "iq",
            "type": "storefronts",
            "href": "/v1/storefronts/iq",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Iraq",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ar"
                ]
            }
        },
        {
            "id": "ie",
            "type": "storefronts",
            "href": "/v1/storefronts/ie",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Ireland",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "il",
            "type": "storefronts",
            "href": "/v1/storefronts/il",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Israel",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "he"
                ]
            }
        },
        {
            "id": "it",
            "type": "storefronts",
            "href": "/v1/storefronts/it",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Italy",
                "defaultLanguageTag": "it",
                "supportedLanguageTags": [
                    "it",
                    "en-GB"
                ]
            }
        },
        {
            "id": "jm",
            "type": "storefronts",
            "href": "/v1/storefronts/jm",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Jamaica",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "jp",
            "type": "storefronts",
            "href": "/v1/storefronts/jp",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Japan",
                "defaultLanguageTag": "ja",
                "supportedLanguageTags": [
                    "ja",
                    "en-US"
                ]
            }
        },
        {
            "id": "jo",
            "type": "storefronts",
            "href": "/v1/storefronts/jo",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Jordan",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ar"
                ]
            }
        },
        {
            "id": "kz",
            "type": "storefronts",
            "href": "/v1/storefronts/kz",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Kazakhstan",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "ke",
            "type": "storefronts",
            "href": "/v1/storefronts/ke",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Kenya",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "kr",
            "type": "storefronts",
            "href": "/v1/storefronts/kr",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Korea, Republic of",
                "defaultLanguageTag": "ko",
                "supportedLanguageTags": [
                    "ko",
                    "en-GB"
                ]
            }
        },
        {
            "id": "xk",
            "type": "storefronts",
            "href": "/v1/storefronts/xk",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Kosovo",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "kw",
            "type": "storefronts",
            "href": "/v1/storefronts/kw",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Kuwait",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ar"
                ]
            }
        },
        {
            "id": "kg",
            "type": "storefronts",
            "href": "/v1/storefronts/kg",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Kyrgyzstan",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "la",
            "type": "storefronts",
            "href": "/v1/storefronts/la",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Lao People’s Democratic Republic",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "lv",
            "type": "storefronts",
            "href": "/v1/storefronts/lv",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Latvia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "lb",
            "type": "storefronts",
            "href": "/v1/storefronts/lb",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Lebanon",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR",
                    "ar"
                ]
            }
        },
        {
            "id": "lr",
            "type": "storefronts",
            "href": "/v1/storefronts/lr",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Liberia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "ly",
            "type": "storefronts",
            "href": "/v1/storefronts/ly",
            "attributes": {
                "explicitContentPolicy": "prohibited",
                "name": "Libya",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ar"
                ]
            }
        },
        {
            "id": "lt",
            "type": "storefronts",
            "href": "/v1/storefronts/lt",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Lithuania",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "lu",
            "type": "storefronts",
            "href": "/v1/storefronts/lu",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Luxembourg",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR",
                    "de-DE"
                ]
            }
        },
        {
            "id": "mo",
            "type": "storefronts",
            "href": "/v1/storefronts/mo",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Macao",
                "defaultLanguageTag": "zh-Hant-HK",
                "supportedLanguageTags": [
                    "zh-Hant-HK",
                    "en-GB",
                    "zh-Hant-TW"
                ]
            }
        },
        {
            "id": "mg",
            "type": "storefronts",
            "href": "/v1/storefronts/mg",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Madagascar",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "mw",
            "type": "storefronts",
            "href": "/v1/storefronts/mw",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Malawi",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "my",
            "type": "storefronts",
            "href": "/v1/storefronts/my",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Malaysia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ms"
                ]
            }
        },
        {
            "id": "mv",
            "type": "storefronts",
            "href": "/v1/storefronts/mv",
            "attributes": {
                "explicitContentPolicy": "prohibited",
                "name": "Maldives",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "ml",
            "type": "storefronts",
            "href": "/v1/storefronts/ml",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Mali",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "mt",
            "type": "storefronts",
            "href": "/v1/storefronts/mt",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Malta",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "mr",
            "type": "storefronts",
            "href": "/v1/storefronts/mr",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Mauritania",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR",
                    "ar"
                ]
            }
        },
        {
            "id": "mu",
            "type": "storefronts",
            "href": "/v1/storefronts/mu",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Mauritius",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "mx",
            "type": "storefronts",
            "href": "/v1/storefronts/mx",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Mexico",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "fm",
            "type": "storefronts",
            "href": "/v1/storefronts/fm",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Micronesia, Federated States of",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "md",
            "type": "storefronts",
            "href": "/v1/storefronts/md",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Moldova",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "mn",
            "type": "storefronts",
            "href": "/v1/storefronts/mn",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Mongolia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "me",
            "type": "storefronts",
            "href": "/v1/storefronts/me",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Montenegro",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "hr"
                ]
            }
        },
        {
            "id": "ms",
            "type": "storefronts",
            "href": "/v1/storefronts/ms",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Montserrat",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "ma",
            "type": "storefronts",
            "href": "/v1/storefronts/ma",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Morocco",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR",
                    "ar"
                ]
            }
        },
        {
            "id": "mz",
            "type": "storefronts",
            "href": "/v1/storefronts/mz",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Mozambique",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "mm",
            "type": "storefronts",
            "href": "/v1/storefronts/mm",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Myanmar",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "na",
            "type": "storefronts",
            "href": "/v1/storefronts/na",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Namibia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "np",
            "type": "storefronts",
            "href": "/v1/storefronts/np",
            "attributes": {
                "explicitContentPolicy": "prohibited",
                "name": "Nepal",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "nl",
            "type": "storefronts",
            "href": "/v1/storefronts/nl",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Netherlands",
                "defaultLanguageTag": "nl",
                "supportedLanguageTags": [
                    "nl",
                    "en-GB"
                ]
            }
        },
        {
            "id": "nz",
            "type": "storefronts",
            "href": "/v1/storefronts/nz",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "New Zealand",
                "defaultLanguageTag": "en-AU",
                "supportedLanguageTags": [
                    "en-AU",
                    "en-GB"
                ]
            }
        },
        {
            "id": "ni",
            "type": "storefronts",
            "href": "/v1/storefronts/ni",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Nicaragua",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "ne",
            "type": "storefronts",
            "href": "/v1/storefronts/ne",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Niger",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "ng",
            "type": "storefronts",
            "href": "/v1/storefronts/ng",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Nigeria",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "mk",
            "type": "storefronts",
            "href": "/v1/storefronts/mk",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "North Macedonia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "no",
            "type": "storefronts",
            "href": "/v1/storefronts/no",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Norway",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "nb"
                ]
            }
        },
        {
            "id": "om",
            "type": "storefronts",
            "href": "/v1/storefronts/om",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Oman",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ar"
                ]
            }
        },
        {
            "id": "pa",
            "type": "storefronts",
            "href": "/v1/storefronts/pa",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Panama",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "pg",
            "type": "storefronts",
            "href": "/v1/storefronts/pg",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Papua New Guinea",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "py",
            "type": "storefronts",
            "href": "/v1/storefronts/py",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Paraguay",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "pe",
            "type": "storefronts",
            "href": "/v1/storefronts/pe",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Peru",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "ph",
            "type": "storefronts",
            "href": "/v1/storefronts/ph",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Philippines",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "pl",
            "type": "storefronts",
            "href": "/v1/storefronts/pl",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Poland",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "pl"
                ]
            }
        },
        {
            "id": "pt",
            "type": "storefronts",
            "href": "/v1/storefronts/pt",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Portugal",
                "defaultLanguageTag": "pt-PT",
                "supportedLanguageTags": [
                    "pt-PT",
                    "en-GB"
                ]
            }
        },
        {
            "id": "qa",
            "type": "storefronts",
            "href": "/v1/storefronts/qa",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Qatar",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ar"
                ]
            }
        },
        {
            "id": "cg",
            "type": "storefronts",
            "href": "/v1/storefronts/cg",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Republic of the Congo",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "ro",
            "type": "storefronts",
            "href": "/v1/storefronts/ro",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Romania",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ro"
                ]
            }
        },
        {
            "id": "ru",
            "type": "storefronts",
            "href": "/v1/storefronts/ru",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Russia",
                "defaultLanguageTag": "ru",
                "supportedLanguageTags": [
                    "ru",
                    "en-GB",
                    "uk"
                ]
            }
        },
        {
            "id": "rw",
            "type": "storefronts",
            "href": "/v1/storefronts/rw",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Rwanda",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "sa",
            "type": "storefronts",
            "href": "/v1/storefronts/sa",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Saudi Arabia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ar"
                ]
            }
        },
        {
            "id": "sn",
            "type": "storefronts",
            "href": "/v1/storefronts/sn",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Senegal",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "rs",
            "type": "storefronts",
            "href": "/v1/storefronts/rs",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Serbia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "hr"
                ]
            }
        },
        {
            "id": "sc",
            "type": "storefronts",
            "href": "/v1/storefronts/sc",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Seychelles",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "sl",
            "type": "storefronts",
            "href": "/v1/storefronts/sl",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Sierra Leone",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "sg",
            "type": "storefronts",
            "href": "/v1/storefronts/sg",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Singapore",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "zh-Hans-CN"
                ]
            }
        },
        {
            "id": "sk",
            "type": "storefronts",
            "href": "/v1/storefronts/sk",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Slovakia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "sk"
                ]
            }
        },
        {
            "id": "si",
            "type": "storefronts",
            "href": "/v1/storefronts/si",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Slovenia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "sb",
            "type": "storefronts",
            "href": "/v1/storefronts/sb",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Solomon Islands",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "za",
            "type": "storefronts",
            "href": "/v1/storefronts/za",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "South Africa",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "es",
            "type": "storefronts",
            "href": "/v1/storefronts/es",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Spain",
                "defaultLanguageTag": "es-ES",
                "supportedLanguageTags": [
                    "es-ES",
                    "en-GB",
                    "ca"
                ]
            }
        },
        {
            "id": "lk",
            "type": "storefronts",
            "href": "/v1/storefronts/lk",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Sri Lanka",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "kn",
            "type": "storefronts",
            "href": "/v1/storefronts/kn",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "St. Kitts and Nevis",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "lc",
            "type": "storefronts",
            "href": "/v1/storefronts/lc",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "St. Lucia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "vc",
            "type": "storefronts",
            "href": "/v1/storefronts/vc",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "St. Vincent and The Grenadines",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "sr",
            "type": "storefronts",
            "href": "/v1/storefronts/sr",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Suriname",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "nl"
                ]
            }
        },
        {
            "id": "se",
            "type": "storefronts",
            "href": "/v1/storefronts/se",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Sweden",
                "defaultLanguageTag": "sv",
                "supportedLanguageTags": [
                    "sv",
                    "en-GB"
                ]
            }
        },
        {
            "id": "ch",
            "type": "storefronts",
            "href": "/v1/storefronts/ch",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Switzerland",
                "defaultLanguageTag": "de-CH",
                "supportedLanguageTags": [
                    "de-CH",
                    "de-DE",
                    "en-GB",
                    "fr-FR",
                    "it"
                ]
            }
        },
        {
            "id": "tw",
            "type": "storefronts",
            "href": "/v1/storefronts/tw",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Taiwan",
                "defaultLanguageTag": "zh-Hant-TW",
                "supportedLanguageTags": [
                    "zh-Hant-TW",
                    "en-GB"
                ]
            }
        },
        {
            "id": "tj",
            "type": "storefronts",
            "href": "/v1/storefronts/tj",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Tajikistan",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "tz",
            "type": "storefronts",
            "href": "/v1/storefronts/tz",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Tanzania",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "th",
            "type": "storefronts",
            "href": "/v1/storefronts/th",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Thailand",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "th"
                ]
            }
        },
        {
            "id": "to",
            "type": "storefronts",
            "href": "/v1/storefronts/to",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Tonga",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "tt",
            "type": "storefronts",
            "href": "/v1/storefronts/tt",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Trinidad and Tobago",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "tn",
            "type": "storefronts",
            "href": "/v1/storefronts/tn",
            "attributes": {
                "explicitContentPolicy": "prohibited",
                "name": "Tunisia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR",
                    "ar"
                ]
            }
        },
        {
            "id": "tr",
            "type": "storefronts",
            "href": "/v1/storefronts/tr",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Turkey",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "tr"
                ]
            }
        },
        {
            "id": "tm",
            "type": "storefronts",
            "href": "/v1/storefronts/tm",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Turkmenistan",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "tc",
            "type": "storefronts",
            "href": "/v1/storefronts/tc",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Turks and Caicos",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "ae",
            "type": "storefronts",
            "href": "/v1/storefronts/ae",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "UAE",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ar"
                ]
            }
        },
        {
            "id": "ug",
            "type": "storefronts",
            "href": "/v1/storefronts/ug",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Uganda",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "ua",
            "type": "storefronts",
            "href": "/v1/storefronts/ua",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Ukraine",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "uk",
                    "ru"
                ]
            }
        },
        {
            "id": "gb",
            "type": "storefronts",
            "href": "/v1/storefronts/gb",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "United Kingdom",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "us",
            "type": "storefronts",
            "href": "/v1/storefronts/us",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "United States",
                "defaultLanguageTag": "en-US",
                "supportedLanguageTags": [
                    "en-US",
                    "es-MX",
                    "ar",
                    "ru",
                    "zh-Hans-CN"
                ]
            }
        },
        {
            "id": "uy",
            "type": "storefronts",
            "href": "/v1/storefronts/uy",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Uruguay",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "es-MX"
                ]
            }
        },
        {
            "id": "uz",
            "type": "storefronts",
            "href": "/v1/storefronts/uz",
            "attributes": {
                "explicitContentPolicy": "prohibited",
                "name": "Uzbekistan",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "vu",
            "type": "storefronts",
            "href": "/v1/storefronts/vu",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Vanuatu",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "fr-FR"
                ]
            }
        },
        {
            "id": "ve",
            "type": "storefronts",
            "href": "/v1/storefronts/ve",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Venezuela",
                "defaultLanguageTag": "es-MX",
                "supportedLanguageTags": [
                    "es-MX",
                    "en-GB"
                ]
            }
        },
        {
            "id": "vn",
            "type": "storefronts",
            "href": "/v1/storefronts/vn",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Vietnam",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "vi"
                ]
            }
        },
        {
            "id": "ye",
            "type": "storefronts",
            "href": "/v1/storefronts/ye",
            "attributes": {
                "explicitContentPolicy": "opt-in",
                "name": "Yemen",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB",
                    "ar"
                ]
            }
        },
        {
            "id": "zm",
            "type": "storefronts",
            "href": "/v1/storefronts/zm",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Zambia",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        },
        {
            "id": "zw",
            "type": "storefronts",
            "href": "/v1/storefronts/zw",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "name": "Zimbabwe",
                "defaultLanguageTag": "en-GB",
                "supportedLanguageTags": [
                    "en-GB"
                ]
            }
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/storefronts`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The next page or group of objects to fetch. See [`Fetching Resources by Page`](fetching-resources-by-page.md).
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Storefronts](storefronts.md)
  A resource object that represents a storefront, an Apple Music and iTunes Store territory that the content is available in.
- [object StorefrontsResponse](storefrontsresponse.md)
  The response to a storefront request.
- [Get a Storefront](get-a-storefront.md)
  Fetch a single storefront by using its identifier.
- [Get Multiple Storefronts](get-multiple-storefronts.md)
  Fetch one or more storefronts by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-storefronts)*